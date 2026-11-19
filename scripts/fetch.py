#!/usr/bin/env python3
"""Stage 1-5 -- fetch, log, clean, deduplicate and archive the VPN Gate list."""
from __future__ import annotations

import argparse
import base64
import hashlib
import os
import re
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def plog(msg):
    print(f"[fetch] {msg}", flush=True)


def looks_like_vpngate_csv(body: bytes) -> bool:
    head = body[:512].lstrip().lower()
    return head.startswith(b"*vpn_servers") or b"#hostname," in head


def try_fetch(timeout: int):
    """Try every known endpoint; return the first response that is real CSV."""
    sess = requests.Session()
    sess.headers.update({"User-Agent": common.USER_AGENT, "Accept": "*/*"})
    retry = requests.adapters.Retry(
        total=3,
        backoff_factor=10,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    adapter = requests.adapters.HTTPAdapter(max_retries=retry)
    sess.mount("http://", adapter)
    sess.mount("https://", adapter)

    last_err = "no endpoint attempted"
    for url in common.ENDPOINTS:
        t0 = time.monotonic()
        try:
            r = sess.get(url, timeout=timeout)
            dur = time.monotonic() - t0
            body = r.content or b""
            ok = r.status_code == 200 and looks_like_vpngate_csv(body)
            plog(
                f"GET {url} -> HTTP {r.status_code}, {len(body):,} bytes "
                f"in {dur:.1f}s, looks_like_csv={ok}"
            )
            if ok:
                return url, r.status_code, body, dur
            last_err = (
                f"{url}: HTTP {r.status_code}, {len(body):,} bytes "
                f"but not VPN Gate CSV (blocked or placeholder page)"
            )
        except Exception as e:  # noqa: BLE001
            last_err = f"{url}: {type(e).__name__}: {e}"
            plog(f"GET {url} -> FAILED {last_err}")
    return None, None, None, last_err


def inject_extra_india_servers(reg: dict, now: str):
    """Pull historical & hidden India (IN) servers from external sources and local fallback_india.ovpn."""
    added = 0

    # 1. Pull from onlyactions/vpngate-monitor latest.json
    try:
        r_ext = requests.get(
            "https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/latest.json",
            timeout=15,
        )
        if r_ext.status_code == 200:
            for srv in r_ext.json():
                if (srv.get("CountryShort") or "").upper() == "IN":
                    test_obj = srv.get("test") or {}
                    via = test_obj.get("via") or ""
                    pr = (test_obj.get("proto") or srv.get("proto") or "tcp").lower()
                    ip = srv.get("IP")
                    port = via.split(":")[1] if ":" in via else (srv.get("port") or srv.get("Port"))
                    host = srv.get("HostName") or f"india-{ip}"
                    if ip and port:
                        key = f"{host}|{ip}"
                        if key not in reg:
                            reg[key] = {
                                **{f: srv.get(f, "") for f in common.PUBLIC_FIELDS},
                                "HostName": host,
                                "IP": ip,
                                "CountryShort": "IN",
                                "CountryLong": "India",
                                "proto": pr,
                                "port": int(port),
                                "first_seen": now,
                                "last_seen": now,
                                "occurrences": 1,
                            }
                            added += 1
    except Exception as e:  # noqa: BLE001
        plog(f"external latest.json India import skipped: {e}")

    # 2. Scrape main VPNGate HTML page for any extra India TCP/UDP ports
    try:
        r_web = requests.get(
            "https://www.vpngate.net/en/",
            headers={"User-Agent": common.USER_AGENT},
            timeout=15,
        )
        if r_web.status_code == 200:
            rows = re.findall(r"<tr.*?>.*?</tr>", r_web.text, re.DOTALL | re.IGNORECASE)
            for row in rows:
                if ">India<" in row or "India (" in row:
                    links = re.findall(
                        r"fqdn=([^&\"']*).*?ip=([^&\"']*).*?tcp=(\d+).*?udp=(\d+)",
                        row,
                    )
                    for fqdn, ip, tcp_p, udp_p in links:
                        host_label = fqdn.split(".")[0] if fqdn else f"india-{ip}"
                        if ip and tcp_p and tcp_p != "0":
                            k_tcp = f"{host_label}-tcp|{ip}"
                            if k_tcp not in reg:
                                reg[k_tcp] = {
                                    "HostName": f"{host_label}-tcp",
                                    "IP": ip,
                                    "Score": 200000,
                                    "Ping": 15,
                                    "Speed": 10000000,
                                    "CountryLong": "India",
                                    "CountryShort": "IN",
                                    "proto": "tcp",
                                    "port": int(tcp_p),
                                    "first_seen": now,
                                    "last_seen": now,
                                    "occurrences": 1,
                                }
                                added += 1
                        if ip and udp_p and udp_p != "0":
                            k_udp = f"{host_label}-udp|{ip}"
                            if k_udp not in reg:
                                reg[k_udp] = {
                                    "HostName": f"{host_label}-udp",
                                    "IP": ip,
                                    "Score": 200000,
                                    "Ping": 15,
                                    "Speed": 10000000,
                                    "CountryLong": "India",
                                    "CountryShort": "IN",
                                    "proto": "udp",
                                    "port": int(udp_p),
                                    "first_seen": now,
                                    "last_seen": now,
                                    "occurrences": 1,
                                }
                                added += 1
    except Exception as e:  # noqa: BLE001
        plog(f"HTML India scrape skipped: {e}")

    # 3. Import existing servers from fallback_india.ovpn so they also get tested
    if os.path.exists("fallback_india.ovpn"):
        try:
            with open("fallback_india.ovpn", "r", encoding="utf-8", errors="ignore") as f:
                ovpn_txt = f.read()
            for m in re.finditer(
                r"^remote\s+([a-zA-Z0-9.-]+)\s+(\d+)(?:\s+(tcp|udp))?",
                ovpn_txt,
                re.MULTILINE | re.IGNORECASE,
            ):
                h_or_ip = m.group(1)
                p = int(m.group(2))
                pr = (m.group(3) or "tcp").lower()
                key = f"fallback-{p}-{pr}|{h_or_ip}"
                if key not in reg:
                    reg[key] = {
                        "HostName": f"fallback-{p}-{pr}",
                        "IP": h_or_ip,
                        "Score": 150000,
                        "Ping": 10,
                        "Speed": 10000000,
                        "CountryLong": "India",
                        "CountryShort": "IN",
                        "proto": pr,
                        "port": p,
                        "first_seen": now,
                        "last_seen": now,
                        "occurrences": 1,
                    }
                    added += 1
                else:
                    reg[key]["last_seen"] = now
        except Exception as e:  # noqa: BLE001
            plog(f"fallback_india.ovpn import error: {e}")

    if added:
        plog(f"India Booster added {added} extra Indian server endpoints to registry")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--archive-dir", default="archive")
    ap.add_argument("--min-rows", type=int, default=common.DEFAULTS["min_rows"])
    ap.add_argument("--keep-archive", type=int, default=common.DEFAULTS["keep_archive"])
    ap.add_argument(
        "--recall-days",
        type=int,
        default=common.DEFAULTS["recall_days"],
        help="keep re-testing servers that appeared in the API within the last N days",
    )
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--from-file", default="", help="debug: use a saved raw API response")
    args = ap.parse_args()

    os.makedirs(os.path.join(args.data_dir, "raw"), exist_ok=True)
    os.makedirs(args.archive_dir, exist_ok=True)
    t_start = time.monotonic()

    # ---- stage 1: fetch (with endpoint fallback + retries) ----------------
    if args.from_file:
        with open(args.from_file, "rb") as f:
            raw = f.read()
        url, status, dur = f"file://{args.from_file}", 0, 0.0
        plog(f"loaded {len(raw):,} bytes from {url} (debug --from-file)")
        if not looks_like_vpngate_csv(raw):
            plog("FATAL --from-file payload is not a VPN Gate CSV")
            return 2
    else:
        url, status, raw, dur = try_fetch(args.timeout)
        if raw is None:
            plog(f"FATAL could not fetch a valid CSV from any endpoint: {dur}")
            return 2
    sha = hashlib.sha256(raw).hexdigest()

    # ---- stage 2: log / persist raw ---------------------------------------
    raw_path = os.path.join(args.data_dir, "raw", "latest.csv")
    common.atomic_write(raw_path, raw)
    plog(f"raw response archived -> {raw_path} ({len(raw):,} bytes, sha256 {sha[:16]}...)")

    # ---- stage 3: clean ----------------------------------------------------
    header, rows, malformed = common.parse_vpngate_csv(raw.decode("utf-8-sig", "replace"))
    plog(f"parsed: rows={len(rows):,} malformed={malformed} header_cols={len(header)}")
    cleaned, bad = [], 0
    for row in rows:
        c = common.clean_row(row)
        if c:
            cleaned.append(c)
        else:
            bad += 1
    plog(f"clean: kept={len(cleaned):,} dropped_invalid={bad}")

    # ---- stage 4: dedupe ---------------------------------------------------
    kept, exact, same_ip = common.dedupe(cleaned)
    plog(f"dedupe: unique={len(kept):,} removed_exact={exact} removed_same_ip={same_ip}")

    if len(kept) < args.min_rows:
        plog(f"FATAL only {len(kept)} valid servers (< {args.min_rows}); refusing to overwrite")
        return 2

    # ---- stage 4b: extract dialable endpoints + shared config template ----
    template = None
    with_endpoint = 0
    for s in kept:
        cfg_text = ""
        try:
            cfg_text = base64.b64decode(s["OpenVPN_ConfigData_Base64"]).decode("utf-8", "replace")
        except Exception:  # noqa: BLE001
            pass
        proto, port = common.extract_proto_port(cfg_text)
        s["_proto"], s["_port"] = proto, port
        if proto and port:
            with_endpoint += 1
            if template is None:
                template = common.extract_template(cfg_text)
    plog(f"endpoints extracted for {with_endpoint}/{len(kept)} servers")
    if template:
        common.atomic_write(os.path.join(args.data_dir, "template.ovpn"), template.encode("utf-8"))

    # ---- stage 4c: registry -- the union of every server ever seen ---------
    reg_path = os.path.join(args.data_dir, "known_servers.json")
    reg = common.load_registry(reg_path)
    now = common.now_iso()
    common.update_registry(reg, kept, now)

    # Run India Booster to inject hidden/historical Indian servers
    inject_extra_india_servers(reg, now)

    dropped = common.prune_registry(reg, args.recall_days)
    common.save_registry(reg_path, reg)
    plog(f"registry: {len(reg):,} known servers (retention {args.recall_days}d, pruned {dropped})")

    plan = common.build_test_plan(reg, kept)
    common.write_json(os.path.join(args.data_dir, "test_plan.json"), plan)
    n_cur = sum(1 for p in plan if p["in_current_list"])
    plog(f"test plan: {len(plan):,} servers ({n_cur:,} current + {len(plan) - n_cur:,} historical)")

    # ---- outputs ------------------------------------------------------------
    csv_path = os.path.join(args.data_dir, "servers_clean.csv")
    common.write_public_csv(csv_path, kept)
    plog(f"wrote {csv_path} ({len(kept):,} rows)")

    meta = {
        "fetched_at": common.now_iso(),
        "source": url,
        "http_status": status,
        "raw_bytes": len(raw),
        "sha256": sha,
        "duration_s": round(dur, 2),
        "rows_parsed": len(rows),
        "rows_malformed": malformed,
        "rows_cleaned": len(cleaned),
        "rows_dropped_invalid": bad,
        "removed_exact_duplicates": exact,
        "removed_same_ip_duplicates": same_ip,
        "unique_servers": len(kept),
        "with_endpoint": with_endpoint,
        "registry_size": len(reg),
        "test_plan_size": len(plan),
        "test_plan_current": n_cur,
        "recall_days": args.recall_days,
    }
    common.write_json(os.path.join(args.data_dir, "last_fetch.json"), meta)

    # ---- stage 5: archive ----------------------------------------------------
    arch = os.path.join(args.archive_dir, f"vpngate_{common.stamp()}.csv.gz")
    common.write_public_csv_gz(arch, kept)
    removed = common.prune_archive(args.archive_dir, args.keep_archive)
    plog(f"archived snapshot -> {arch} (pruned {removed} old snapshots)")

    plog(f"DONE in {time.monotonic() - t_start:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
