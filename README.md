# 🛡️ VPN Gate Monitor

> **Once a day** this repo fetches the complete public [VPN Gate](https://www.vpngate.net/en/) server list, **cleans, deduplicates and archives** it — and then does the part that matters: it **opens a real OpenVPN tunnel to every single listed server**, verifies that traffic genuinely exits through it, checks *where* it exits, and measures real download throughput.
>
> **Everything below this line is the auto-generated living report. No hand-edited numbers.**

[![pipeline](https://github.com/bhaylorina/vpngate-monitor/actions/workflows/vpngate.yml/badge.svg)](https://github.com/bhaylorina/vpngate-monitor/actions/workflows/vpngate.yml)
[![servers tracked](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fbhaylorina%2Fvpngate-monitor%2Fmain%2Fbadges%2Fservers.json)](https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/badges/servers.json)
[![verified alive](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fbhaylorina%2Fvpngate-monitor%2Fmain%2Fbadges%2Falive.json)](https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/badges/alive.json)
[![avg measured speed](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fbhaylorina%2Fvpngate-monitor%2Fmain%2Fbadges%2Fspeed.json)](https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/badges/speed.json)
[![last run](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fbhaylorina%2Fvpngate-monitor%2Fmain%2Fbadges%2Fupdated.json)](https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/badges/updated.json)

## 📊 Latest results

| | |
|---|---|
| **Run** | [#9 · view run](https://github.com/bhaylorina/vpngate-monitor/actions/runs/44680980547) · 2026-11-20 05:26:14 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **93** |
| **Duplicates removed** | 0 exact + 2 same-IP |
| **Servers tested** | **4 of 1,499** — all 93 current + 1,406 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **3** — 0 from the current list + 3 historical ♻️ |
| **❌ Dead / unusable** | 1 |
| **Usability** | **0.0%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **9.3 / 10.7 / 11.1 Mbps** |
| **🚀 Fastest verified** | **vpn368881682** · 🇮🇳 India · **11.1 Mbps** |
| **🧭 Exit-country mismatches** | 0 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.7 s |
| **Untested** | 1,495 |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn368881682` | 🇮🇳 India | ♻️ historical | `106.51.189.183:1531`/tcp | 4.3s | **11.1 Mbps** | 79.2 Mbps | 605,665 |
| 2 | `vpn359610091-udp` | 🇮🇳 India | ♻️ historical | `103.172.220.133:1195`/udp | 2.5s | **10.7 Mbps** | 10.0 Mbps | 150,000 |
| 3 | `vpn359610091` | 🇮🇳 India | ♻️ historical | `103.172.220.133:995`/tcp | 4.3s | **6.0 Mbps** | 7.6 Mbps | 1,215,566 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `vpn359610091` | 🇮🇳 IN | 1,215,566 | 7.6 Mbps | 6.0 Mbps | 74 | 40.0 d | 2weeks |
| 2 | `vpn368881682` | 🇮🇳 IN | 605,665 | 79.2 Mbps | 11.1 Mbps | 28 | 0.0 h | 2weeks |
| 3 | `vpn359610091-udp` | 🇮🇳 IN | 150,000 | 10.0 Mbps | 10.7 Mbps | 1 | 1.0 h | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 665 | 0 | 0.0 Mbps | `` |
| 🇰🇷 Korea Republic of (KR) | 515 | 0 | 0.0 Mbps | `` |
| 🇷🇺 Russian Federation (RU) | 128 | 0 | 0.0 Mbps | `` |
| 🇹🇭 Thailand (TH) | 60 | 0 | 0.0 Mbps | `` |
| 🇺🇸 United States (US) | 36 | 0 | 0.0 Mbps | `` |
| 🇻🇳 Viet Nam (VN) | 17 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 7 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 6 | 0 | 0.0 Mbps | `` |
| 🇮🇳 India (IN) | 6 | 3 | 11.1 Mbps | `vpn368881682` |
| 🇦🇷 Argentina (AR) | 5 | 0 | 0.0 Mbps | `` |
| 🇬🇧 United Kingdom (GB) | 4 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 4 | 0 | 0.0 Mbps | `` |
| 🇮🇩 Indonesia (ID) | 3 | 0 | 0.0 Mbps | `` |
| 🇲🇲 Myanmar (MM) | 3 | 0 | 0.0 Mbps | `` |
| 🇲🇽 Mexico (MX) | 3 | 0 | 0.0 Mbps | `` |
| 🇧🇾 Belarus (BY) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇦 Canada (CA) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 2 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 2 | 0 | 0.0 Mbps | `` |
| 🇭🇰 Hong Kong (HK) | 2 | 0 | 0.0 Mbps | `` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 2 | 0 | 0.0 Mbps | `` |
| 🇲🇾 Malaysia (MY) | 2 | 0 | 0.0 Mbps | `` |
| 🇳🇿 New Zealand (NZ) | 2 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 2 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 2 | 0 | 0.0 Mbps | `` |
| 🇻🇪 Venezuela (VE) | 2 | 0 | 0.0 Mbps | `` |
| 🇦🇪 United Arab Emirates (AE) | 1 | 0 | 0.0 Mbps | `` |
| 🇦🇹 Austria (AT) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇪 Estonia (EE) | 1 | 0 | 0.0 Mbps | `` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇮🇹 Italy (IT) | 1 | 0 | 0.0 Mbps | `` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇻 Latvia (LV) | 1 | 0 | 0.0 Mbps | `` |
| 🇳🇱 Netherlands (NL) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇦 Panama (PA) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇸 Palestinian Territory Occupied (PS) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇹 Portugal (PT) | 1 | 0 | 0.0 Mbps | `` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |
| 🇸🇪 Sweden (SE) | 1 | 0 | 0.0 Mbps | `` |
| … | +1 more countries | | | |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn368881682` | 🇮🇳 IN | 79 Mbps | 11.1 Mbps | 14% |
| `vpn359610091` | 🇮🇳 IN | 8 Mbps | 6.0 Mbps | 79% |
| `vpn359610091-udp` | 🇮🇳 IN | 10 Mbps | 10.7 Mbps | 107% |

Most honest of this round: `vpn359610091-udp` (11 Mbps), `vpn359610091` (6 Mbps), `vpn368881682` (11 Mbps).

## 🧭 Exit-country mismatches

. ✅ Every verified server exits where it claims.

## 📈 History

Alive % trend (last 32 runs): `██▇▆▆▁▄▅▄▄▄█▄▄▄▄▄▄▄▄▃▃▃▃▃▁▁▁██▅█`

Avg measured speed (Mbps): `▄▄▁▄▁▅▅▄▁▃▁▄▃▄▄▅▄██▄▅▇▃▇▄▂▂█▅▄▆▇`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-11-19 20:31:01 UTC | 96 | 3 | 75% | 14.0 | 15.5 | 0 |
| 2026-11-19 18:53:14 UTC | 93 | 2 | 50% | 13.7 | 16.5 | 0 |
| 2026-11-19 18:45:37 UTC | 92 | 3 | 75% | 11.8 | 15.1 | 0 |
| 2026-11-19 18:37:28 UTC | 89 | 7 | 70% | 12.4 | 16.1 | 0 |
| 2026-11-19 18:30:09 UTC | 93 | 2 | 25% | 15.5 | 16.4 | 0 |
| 2026-11-19 18:23:08 UTC | 96 | 1 | 25% | 9.6 | 9.6 | 0 |
| 2026-11-19 17:51:08 UTC | 98 | 356 | 31% | 10.3 | 33.1 | 4 |
| 2026-11-19 04:25:57 UTC | 95 | 429 | 40% | 11.4 | 47.3 | 3 |
| 2026-11-18 04:22:25 UTC | 92 | 389 | 39% | 14.2 | 37.8 | 2 |
| 2026-11-17 04:21:05 UTC | 98 | 397 | 42% | 11.0 | 26.6 | 3 |
| 2026-11-16 04:58:07 UTC | 94 | 366 | 42% | 14.3 | 35.9 | 1 |
| 2026-11-15 04:20:41 UTC | 90 | 334 | 41% | 12.4 | 29.8 | 0 |
| 2026-11-14 04:17:29 UTC | 98 | 323 | 44% | 11.3 | 54.8 | 2 |
| 2026-11-13 04:22:35 UTC | 97 | 295 | 44% | 14.9 | 46.8 | 1 |
| 2026-11-12 04:23:10 UTC | 93 | 272 | 46% | 15.0 | 29.9 | 0 |

## ⚙️ How the pipeline works

```mermaid
flowchart LR
    C["cron: daily 03:23 UTC"] --> F["fetch vpngate.net CSV API"]
    F --> L["log raw + meta"]
    L --> CL["clean + type-check"]
    CL --> D["dedupe hostname + IP"]
    D --> A["archive .csv.gz snapshot"]
    D --> T["REAL test: OpenVPN tunnel per server<br/>egress + geo + throughput"]
    T --> R["report: README + badges + history"]
    R --> P["commit and push"]
```

1. **Fetch** — `GET /api/iphone/` with retries and endpoint fallback; responses are validated (the API sometimes serves an empty placeholder page to datacenter IPs) and the raw bytes are logged and hashed (sha256).
2. **Clean** — parse the special CSV (`*vpn_servers` marker, `#`-prefixed header), type-check every numeric field, validate IPs, drop broken rows, strip noise.
3. **Dedupe** — remove exact `(HostName, IP)` duplicates, then same-IP entries keeping the highest-scoring one.
4. **Archive** — every run writes an immutable gzipped snapshot to `archive/` (auto-pruned to the newest 360 ≈ 90 days).
5. **Test — the real deal.** For **every** server, every run — not just the API's current list, but **the union of every server that has ever appeared** within the 30-day recall window (kept in `data/known_servers.json`): decode the shared VPN Gate OpenVPN template (all servers ship the same CA + dummy client cert — verified), rebuild each server's config with its remembered `(proto, port)`, force it onto a per-worker `tun` device, disable pushed routes, pin two /32 routes through the tunnel to per-worker Cloudflare anycast IPs, wait for *Initialization Sequence Completed*, then verify egress (`cdn-cgi/trace` through the tunnel must return a foreign exit IP + real exit country) and measure a 5 MB download through the same tunnel. Up to 48 isolated tunnels run in parallel; a server that never completes the handshake is hard-killed after 25 s.
6. **Report** — this README, four live badges, `latest.json`, `summary.json` and the `history.jsonl` log are regenerated and committed by `github-actions[bot]`.

## 📁 Data files & programmatic use

All results are in this repo — hotlink them straight from `https://github.com/bhaylorina/vpngate-monitor`:

- [`data/latest.json`](https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/data/latest.json) — the merged dataset: every cleaned server + its latest real test result
- [`data/servers_clean.csv`](https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/data/servers_clean.csv) — cleaned, deduplicated server list (no bulky config blobs)
- [`data/summary.json`](https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/data/summary.json) — compact run summary with failure breakdown
- [`data/history.jsonl`](https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/data/history.jsonl) — one JSON line per run, append-only
- [`archive/`](https://github.com/bhaylorina/vpngate-monitor/tree/main/archive) — immutable gzipped snapshots of every run
- full logs, raw API response and per-server error details are attached to each [Actions run](https://github.com/bhaylorina/vpngate-monitor/actions) as artifacts (30-day retention)

Grab a working VPN right now:

```bash
curl -s https://raw.githubusercontent.com/bhaylorina/vpngate-monitor/main/data/latest.json \
  | python3 -c "import json,sys;[print(s['IP'],s['CountryShort'],s['test']['download_mbps'],'Mbps') for s in json.load(sys.stdin) if s['test'] and s['test']['alive']]" \
  | sort -k3 -nr | head
```

Field units: `Score` points · `Ping` ms · `Speed` bit/s (self-reported) · `Uptime` ms · `TotalUsers` count · `TotalTraffic` bytes · `download_mbps` Mbps (measured through the tunnel).

## 🔬 Methodology & caveats

- **Real tunnels, not CSV checks.** A server only counts as alive if OpenVPN completed its handshake *and* an HTTPS request bound to the tunnel egressed with a foreign IP. A server whose tunnel silently black-holes traffic fails the egress step and is reported dead.
- **No DNS through the VPN.** Test destinations are pinned with `curl --resolve` to per-worker Cloudflare anycast addresses, so a broken/hijacking VPN DNS can never fake a success.
- **Throughput** is one 5 MB download to `speed.cloudflare.com` through the live tunnel — a sample, not a lab measurement.
- **Vantage point**: GitHub Actions runners (Azure, usually US/EU). A server that is slow from there may be fast from your country, and vice versa.
- **Fairness**: volunteer servers are shared — measured speeds dip when many clients are connected (`NumVpnSessions` is listed).
- **Security**: test traffic is TLS to Cloudflare only; we never send anything sensitive through volunteer servers. Neither should you — assume the operator can see traffic metadata.

## ⚠️ Disclaimer

- [VPN Gate](https://www.vpngate.net/en/) is an academic experiment by the University of Tsukuba, Japan (Daiyuu Nobori & co). This project is an independent monitor of its public API and is **not affiliated** with it.
- VPN servers are run by volunteers; some keep connection logs (see `LogType`). Use them legally and responsibly; do not route anything private or illegal through them.
- Data is provided **as-is** for research/educational purposes.

## 📄 License

Code: MIT. Data: originates from VPN Gate's public API — respect their terms.

---
*Auto-generated by [run #9](https://github.com/bhaylorina/vpngate-monitor/actions/runs/44680980547) at 2026-11-20 05:26:47 UTC. Next scheduled run: daily at 03:23 UTC.*
