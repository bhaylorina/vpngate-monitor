#!/usr/bin/env python3
"""Stage 6 -- test the VPNs FOR REAL and build fallback_india.ovpn."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

TMP_ROOT = "/tmp/vpmon"

DEV_RE = re.compile(r"(?mi)^\s*dev\s+\S+\s*$")

ERROR_PATTERNS = [
    ("AUTH_FAILED", "auth_failed"),
    ("Connection refused", "connection_refused"),
    ("timed out", "timeout"),
    ("tls key negotiation failed", "tls_handshake_failed"),
    ("certificate verification failed", "cert_verification_failed"),
    ("certificate is expired", "cert_expired"),
    ("Cannot resolve host", "dns_failure"),
    ("unknown option", "options_error"),
    ("Cannot open file", "file_error"),
    ("Neither IPv4 nor IPv6", "no_route_to_host"),
    ("errno=111", "connection_refused"),
    ("errno=113", "no_route_to_host"),
    ("TUN/TAP device", "tun_error"),
    ("Cipher", "cipher_error"),
]

PRINT_LOCK = threading.Lock()
FLUSH_LOCK = threading.Lock()
STOP = threading.Event()
RESULTS: list = []
DONE = {"n": 0, "alive": 0}


def plog(msg):
    with PRINT_LOCK:
        print(f"[test ] {msg}", flush=True)


def openvpn_version():
    try:
        out = subprocess.run(
            ["openvpn", "--version"], capture_output=True, text=True, timeout=15
        ).stdout
        m = re.search(r"OpenVPN (\d+)\.(\d+)", out)
        if m:
            return int(m.group(1)), int(m.group(2))
    except Exception:  # noqa: BLE001
        pass
    return None


def build_config(template: str, proto: str, ip: str, port: int, worker: int, ov_ver) -> str:
    """Assemble a hardened test config: shared template + endpoint + per-worker tun device."""
    tun = common.worker_tun(worker)
    cfg = f"proto {proto}\nremote {ip} {port}\n" + template
    cfg, n = DEV_RE.subn(f"dev {tun}", cfg, count=1)
    if n == 0:
        cfg = f"dev {tun}\n{cfg}"

    cf1, cf2 = common.worker_cf_ips(worker)
    extra = [
        "route-nopull",
        f"route {cf1} 255.255.255.255",
        f"route {cf2} 255.255.255.255",
        "verb 3",
        "mute-replay-warnings",
        "auth-nocache",
        "resolv-retry 2",
        "tls-version-min 1.0",
        "tls-cipher DEFAULT:@SECLEVEL=0",
    ]
    if ov_ver and ov_ver >= (2, 4):
        extra.append("tls-cert-profile insecure")
    if ov_ver and ov_ver >= (2, 5):
        extra.append("data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305:AES-128-CBC")
        extra.append("data-ciphers-fallback AES-128-CBC")
    return cfg.rstrip() + "\n" + "\n".join(extra) + "\n"


def classify_error(log_text: str) -> str:
    for needle, code in ERROR_PATTERNS:
        if needle.lower() in log_text.lower():
            return code
    lines = [l.strip() for l in log_text.splitlines() if l.strip()]
    if lines:
        return "died: " + lines[-1][:140]
    return "died_without_log"


def wait_up(log_path, proc, timeout):
    """Poll the openvpn log until the tunnel is really up."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with open(log_path, "r", errors="replace") as f:
                txt = f.read()
        except (FileNotFoundError, PermissionError):
            txt = ""
        if "Initialization Sequence Completed" in txt:
            return True, "up"
        if proc.poll() is not None:
            return False, classify_error(txt)
        time.sleep(0.25)
    return False, "connect_timeout"


def kill_proc(proc):
    if proc is None:
        return
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    except Exception:  # noqa: BLE001
        try:
            proc.terminate()
        except Exception:  # noqa: BLE001
            pass
    try:
        proc.wait(4)
    except Exception:  # noqa: BLE001
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except Exception:  # noqa: BLE001
            pass
        try:
            proc.wait(3)
        except Exception:  # noqa: BLE001
            pass


def run_curl(args_list, hard_timeout):
    cmd = ["curl", "-sS", "-4", "-L", *args_list]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=hard_timeout)
        return p.returncode, p.stdout, (p.stderr or "").strip()
    except subprocess.TimeoutExpired:
        return 124, "", "harness hard timeout"


def http_via_tunnel(tun, cf_ips, timeout):
    """Fetch cloudflare's cdn-cgi/trace through the tunnel; returns exit info."""
    for cf in cf_ips:
        rc, out, err = run_curl(
            [
                "--max-time",
                str(timeout),
                "--interface",
                tun,
                "--resolve",
                f"www.cloudflare.com:443:{cf}",
                "-w",
                "\n__META__%{time_total}",
                "https://www.cloudflare.com/cdn-cgi/trace",
            ],
            timeout + 6,
        )
        if rc == 0 and "__META__" in out:
            body, _, t = out.rpartition("__META__")
            fields = {}
            for line in body.strip().splitlines():
                if "=" in line:
                    k, v = line.split("=", 1)
                    fields[k] = v
            if fields.get("ip"):
                try:
                    t = float(t)
                except ValueError:
                    t = None
                return {
                    "ip": fields["ip"],
                    "loc": fields.get("loc", "??"),
                    "time": t,
                    "cf": cf,
                }
    return None


def speed_via_tunnel(tun, cf, args):
    rc, out, err = run_curl(
        [
            "--max-time",
            str(args.speed_timeout),
            "--interface",
            tun,
            "--resolve",
            f"speed.cloudflare.com:443:{cf}",
            "-o",
            "/dev/null",
            "-w",
            "%{size_download} %{time_total}",
            f"https://speed.cloudflare.com/__down?bytes={args.speed_bytes}",
        ],
        args.speed_timeout + 8,
    )
    parts = out.split()
    if len(parts) == 2:
        try:
            size, t = float(parts[0]), float(parts[1])
            if size > 100_000 and t > 0:
                return {
                    "download_mbps": round(size * 8 / t / 1e6, 2),
                    "downloaded_bytes": int(size),
                    "speed_capped": rc == 28,
                }
        except ValueError:
            pass
    return {"speed_error": (err or f"curl_rc_{rc}")[:100]}


def get_runner_ip():
    rc, out, _ = run_curl(
        ["--max-time", "10", "https://www.cloudflare.com/cdn-cgi/trace"], 15
    )
    if rc == 0:
        for line in out.splitlines():
            if line.startswith("ip="):
                return line.split("=", 1)[1].strip()
    return None


def test_server(s, worker, runner_ip, args, ov_ver, template):
    seq = s["_seq"]
    base = {
        "HostName": s["HostName"],
        "IP": s["IP"],
        "in_current_list": bool(s.get("in_current_list")),
    }
    try:
        proto, ip, port = s.get("proto"), s["IP"], s.get("port")
        if not proto or not port:
            return {**base, "alive": False, "error": "no_known_endpoint"}

        cfg = build_config(template, proto, ip, int(port), worker, ov_ver)
        base["via"] = f"{ip}:{port}"
        base["proto"] = proto

        cf_ips = common.worker_cf_ips(worker)
        tun = common.worker_tun(worker)
        d = tempfile.mkdtemp(prefix=f"vpmon{seq:06d}-", dir=TMP_ROOT)
        cfgp, logp = os.path.join(d, "client.ovpn"), os.path.join(d, "openvpn.log")
        with open(cfgp, "w") as f:
            f.write(cfg)

        t0 = time.monotonic()
        proc = subprocess.Popen(
            ["openvpn", "--config", cfgp, "--log", logp],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        try:
            ok, reason = wait_up(logp, proc, args.connect_timeout)
            base["connect_ms"] = round((time.monotonic() - t0) * 1000)
            if not ok:
                base.update(alive=False, error=reason)
                return base

            for cf in cf_ips:
                subprocess.run(
                    [
                        "ip",
                        "route",
                        "replace",
                        f"{cf}/32",
                        "dev",
                        tun,
                        "metric",
                        str(5000 + worker),
                    ],
                    capture_output=True,
                )

            trace = http_via_tunnel(tun, cf_ips, args.trace_timeout)
            if trace is None:
                base.update(alive=False, error="egress_verification_failed")
                return base
            base.update(
                exit_ip=trace["ip"],
                exit_country=trace["loc"],
                http_s=trace["time"],
            )
            if runner_ip and trace["ip"] == runner_ip:
                base.update(alive=False, error="tunnel_not_used_egress_is_runner_ip")
                return base

            base["alive"] = True
            base["geo_match"] = trace["loc"] == (s.get("CountryShort") or "").strip().upper()
            base.update(speed_via_tunnel(tun, trace["cf"], args))
            return base
        finally:
            kill_proc(proc)
            shutil.rmtree(d, ignore_errors=True)
    except Exception as e:  # noqa: BLE001
        return {
            **base,
            "alive": False,
            "error": f"harness_error:{type(e).__name__}:{str(e)[:120]}",
        }


def flush_results(path, servers_meta, args, runner_ip, partial):
    results = list(RESULTS)
    alive = sum(1 for r in results if r.get("alive"))
    totals = {
        "tested": len(results),
        "alive": alive,
        "dead": len(results) - alive,
        "geo_mismatch": sum(
            1 for r in results if r.get("alive") and r.get("geo_match") is False
        ),
        "partial": partial,
    }
    doc = {
        "generated_at": common.now_iso(),
        "runner_ip": runner_ip,
        "params": {
            k: getattr(args, k)
            for k in (
                "workers",
                "max_servers",
                "connect_timeout",
                "trace_timeout",
                "speed_bytes",
                "speed_timeout",
            )
        },
        "totals": totals,
        "results": results,
    }
    with FLUSH_LOCK:
        common.write_json(path, doc)
    return totals


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--workers", type=int, default=common.DEFAULTS["workers"])
    ap.add_argument(
        "--max-servers",
        type=int,
        default=0,
        help="0 = test every single matching server",
    )
    ap.add_argument(
        "--countries",
        default="",
        help="optional comma-separated CountryShort filter (e.g. IN)",
    )
    ap.add_argument("--connect-timeout", type=int, default=common.DEFAULTS["connect_timeout"])
    ap.add_argument("--trace-timeout", type=int, default=common.DEFAULTS["trace_timeout"])
    ap.add_argument("--speed-bytes", type=int, default=common.DEFAULTS["speed_bytes"])
    ap.add_argument("--speed-timeout", type=int, default=common.DEFAULTS["speed_timeout"])
    ap.add_argument("--flush-every", type=int, default=50)
    ap.add_argument("--max-total-minutes", type=int, default=75)
    args = ap.parse_args()

    if os.geteuid() != 0:
        print("ERROR: run me as root (sudo)", flush=True)
        return 3
    ov_ver = openvpn_version()
    if ov_ver is None:
        print("ERROR: openvpn not found on PATH", flush=True)
        return 3
    plog(f"openvpn {ov_ver[0]}.{ov_ver[1]} detected")

    tpl_path = os.path.join(args.data_dir, "template.ovpn")
    plan_path = os.path.join(args.data_dir, "test_plan.json")
    out_path = os.path.join(args.data_dir, "results.json")

    if not os.path.exists(plan_path) or not os.path.exists(tpl_path):
        plog(f"FATAL {plan_path} or {tpl_path} missing -- run scripts/fetch.py first")
        return 1
    with open(tpl_path, encoding="utf-8") as f:
        template = f.read()
    with open(plan_path, encoding="utf-8") as f:
        servers = json.load(f)
    for i, s in enumerate(servers):
        s["_seq"] = i

    if args.countries:
        want = {c.strip().upper() for c in args.countries.split(",") if c.strip()}
        servers = [
            s for s in servers if (s.get("CountryShort") or "").upper() in want
        ]
    if args.max_servers and args.max_servers > 0:
        servers = servers[: args.max_servers]

    runner_ip = get_runner_ip()

    if not servers:
        plog("No matching servers found to test right now -- exiting cleanly")
        flush_results(out_path, None, args, runner_ip, partial=False)
        return 0

    args.workers = max(1, min(args.workers, 200))
    os.makedirs(TMP_ROOT, exist_ok=True)

    plog(f"runner ip: {runner_ip}")
    n_cur = sum(1 for s in servers if s.get("in_current_list"))
    plog(
        f"testing {len(servers):,} servers ({n_cur:,} current + "
        f"{len(servers) - n_cur:,} historical) with {args.workers} isolated tunnels"
    )

    slots = __import__("queue").Queue()
    for w in range(args.workers):
        slots.put(w)

    def on_term(signum, _frame):
        STOP.set()
        plog(f"signal {signum} received -- stopping, flushing partial results")
        flush_results(out_path, None, args, runner_ip, partial=True)
        subprocess.run(["pkill", "-f", TMP_ROOT], capture_output=True)
        sys.exit(128 + signum)

    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)

    deadline = time.monotonic() + args.max_total_minutes * 60

    def wrapped(s):
        if STOP.is_set():
            return {
                "HostName": s["HostName"],
                "IP": s["IP"],
                "in_current_list": bool(s.get("in_current_list")),
                "alive": False,
                "error": "skipped_deadline",
            }
        w = slots.get()
        try:
            return test_server(s, w, runner_ip, args, ov_ver, template)
        finally:
            slots.put(w)

    t_start = time.monotonic()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(wrapped, s) for s in servers]
        for fut in as_completed(futures):
            r = fut.result()
            with FLUSH_LOCK:
                RESULTS.append(r)
                DONE["n"] += 1
                if r.get("alive"):
                    DONE["alive"] += 1
            if time.monotonic() > deadline and not STOP.is_set():
                STOP.set()
                plog("global time budget reached -- no new tests will start")
            n, a = DONE["n"], DONE["alive"]
            if r.get("alive"):
                plog(
                    f"[{n}/{len(servers)}] ALIVE {r['HostName']} ({r['IP']}) "
                    f"exit={r.get('exit_ip')} {r.get('exit_country')} "
                    f"speed={r.get('download_mbps', '?')} Mbps"
                )
            elif n % 5 == 0 or n == len(servers):
                plog(f"[{n}/{len(servers)}] progress: {a} alive so far")
            if n % args.flush_every == 0:
                flush_results(out_path, None, args, runner_ip, partial=True)

    totals = flush_results(out_path, None, args, runner_ip, partial=False)

    sudo_uid = os.environ.get("SUDO_UID")
    if sudo_uid and sudo_uid.isdigit():
        for p in (out_path,):
            try:
                os.chown(p, int(sudo_uid), -1)
            except OSError:
                pass

    subprocess.run(["pkill", "-f", TMP_ROOT], capture_output=True)
    shutil.rmtree(TMP_ROOT, ignore_errors=True)

    alive = [r for r in RESULTS if r.get("alive")]
    plog("=" * 64)
    plog(
        f"TESTED {totals['tested']:,} servers in "
        f"{(time.monotonic() - t_start):.1f} sec | ALIVE: {totals['alive']:,}"
    )

    # ---- AUTO-GENERATE fallback_india.ovpn (Fastest Verified Alive at Top!) ----
    if alive and template:
        alive_sorted = sorted(alive, key=lambda x: -(x.get("download_mbps") or 0))
        remote_lines = []
        seen_rem = set()
        for r in alive_sorted:
            via = r.get("via") or f"{r['IP']}:443"
            proto = (r.get("proto") or "tcp").lower()
            if ":" in via:
                h, p = via.split(":", 1)
                line = f"remote {h} {p} {proto}"
                if line not in seen_rem:
                    seen_rem.add(line)
                    remote_lines.append(line)

        if remote_lines:
            clean_tpl = re.sub(r"(?mi)^\s*client\s*$", "", template).strip()
            final_ovpn = (
                "client\ndev tun\nproto udp\n"
                + "\n".join(remote_lines)
                + "\n\n"
                + clean_tpl
                + "\n"
            )
            with open("fallback_india.ovpn", "w", encoding="utf-8") as f:
                f.write(final_ovpn)
            if sudo_uid and sudo_uid.isdigit():
                try:
                    os.chown("fallback_india.ovpn", int(sudo_uid), -1)
                except OSError:
                    pass
            plog(f"SUCCESS! Wrote fallback_india.ovpn with {len(remote_lines)} working Indian server(s)!")
    else:
        plog("No live Indian servers answered this round; keeping existing fallback_india.ovpn untouched.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
