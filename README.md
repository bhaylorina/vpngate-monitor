# 🛡️ VPN Gate Monitor

> **Once a day** this repo fetches the complete public [VPN Gate](https://www.vpngate.net/en/) server list, **cleans, deduplicates and archives** it — and then does the part that matters: it **opens a real OpenVPN tunnel to every single listed server**, verifies that traffic genuinely exits through it, checks *where* it exits, and measures real download throughput.
>
> **Everything below this line is the auto-generated living report. No hand-edited numbers.**

[![pipeline](https://github.com/onlyactions/vpngate-monitor/actions/workflows/vpngate.yml/badge.svg)](https://github.com/onlyactions/vpngate-monitor/actions/workflows/vpngate.yml)
[![servers tracked](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fservers.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/servers.json)
[![verified alive](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Falive.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/alive.json)
[![avg measured speed](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fspeed.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/speed.json)
[![last run](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fupdated.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/updated.json)

## 📊 Latest results

| | |
|---|---|
| **Run** | [#11 · view run](https://github.com/onlyactions/vpngate-monitor/actions/runs/43807198337) · 2026-11-16 04:58:07 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **94** |
| **Duplicates removed** | 0 exact + 0 same-IP |
| **Servers tested** | **880 of 880** — all 94 current + 786 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **366** — 69 from the current list + 297 historical ♻️ |
| **❌ Dead / unusable** | 514 |
| **Usability** | **73.4%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **14.3 / 15.8 / 35.9 Mbps** |
| **🚀 Fastest verified** | **vpn367633262** · 🇯🇵 Japan · **35.9 Mbps** |
| **🧭 Exit-country mismatches** | 1 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.1 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn367633262` | 🇯🇵 Japan | ♻️ historical | `138.64.87.141:39975`/udp | 2.3s | **35.9 Mbps** | 665.7 Mbps | 670,751 |
| 2 | `vpn201737691` | 🇯🇵 Japan | ♻️ historical | `59.85.16.253:1742`/udp | 2.3s | **35.2 Mbps** | 598.5 Mbps | 1,505,888 |
| 3 | `vpn909153861` | 🇯🇵 Japan | ♻️ historical | `138.64.96.118:14355`/udp | 2.3s | **33.7 Mbps** | 194.2 Mbps | 812,170 |
| 4 | `vpn702119480` | 🇯🇵 Japan | 📋 current | `118.105.160.215:1958`/udp | 2.5s | **32.8 Mbps** | 833.4 Mbps | 611,183 |
| 5 | `vpn526062445` | 🇯🇵 Japan | ♻️ historical | `60.143.120.123:1632`/udp | 2.5s | **29.9 Mbps** | 538.8 Mbps | 1,465,451 |
| 6 | `vpn459755685` | 🇯🇵 Japan | ♻️ historical | `180.43.107.71:1563`/udp | 2.5s | **28.5 Mbps** | 95.9 Mbps | 625,821 |
| 7 | `vpn711923274` | 🇰🇷 Korea Republic of | ♻️ historical | `59.12.180.71:1625`/udp | 2.5s | **25.7 Mbps** | 44.0 Mbps | 523,019 |
| 8 | `vpn767018401` | 🇯🇵 Japan | ♻️ historical | `113.197.44.139:1233`/udp | 2.3s | **25.4 Mbps** | 82.0 Mbps | 576,440 |
| 9 | `vpn106798950` | 🇯🇵 Japan | ♻️ historical | `118.240.49.38:1688`/tcp | 2.8s | **25.1 Mbps** | 296.2 Mbps | 715,747 |
| 10 | `vpn152067795` | 🇰🇷 Korea Republic of | 📋 current | `180.231.86.46:1532`/udp | 2.3s | **24.9 Mbps** | 95.6 Mbps | 479,387 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-100` | 🇯🇵 JP | 3,003,937 | 236.1 Mbps | 22.0 Mbps | 179 | 16.9 d | 2weeks |
| 2 | `public-vpn-82` | 🇯🇵 JP | 2,929,422 | 293.8 Mbps | 3.1 Mbps | 80 | 22.9 d | 2weeks |
| 3 | `public-vpn-258` | 🇯🇵 JP | 2,927,383 | 194.9 Mbps | 10.1 Mbps | 64 | 16.9 d | 2weeks |
| 4 | `public-vpn-154` | 🇯🇵 JP | 2,864,520 | 208.0 Mbps | 19.3 Mbps | 104 | 19.9 d | 2weeks |
| 5 | `public-vpn-78` | 🇯🇵 JP | 2,853,500 | 294.3 Mbps | 21.2 Mbps | 126 | 14.9 d | 2weeks |
| 6 | `public-vpn-200` | 🇯🇵 JP | 2,846,412 | 177.2 Mbps | 14.2 Mbps | 51 | 18.9 d | 2weeks |
| 7 | `public-vpn-117` | 🇯🇵 JP | 2,788,135 | 203.1 Mbps | 15.4 Mbps | 38 | 22.9 d | 2weeks |
| 8 | `public-vpn-39` | 🇯🇵 JP | 2,787,871 | 228.2 Mbps | 21.4 Mbps | 137 | 14.9 d | 2weeks |
| 9 | `public-vpn-134` | 🇯🇵 JP | 2,748,495 | 241.4 Mbps | 13.9 Mbps | 56 | 14.9 d | 2weeks |
| 10 | `public-vpn-133` | 🇯🇵 JP | 2,715,398 | 226.0 Mbps | 21.7 Mbps | 65 | 21.9 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 404 | 178 | 35.9 Mbps | `vpn367633262` |
| 🇰🇷 Korea Republic of (KR) | 287 | 139 | 25.7 Mbps | `vpn711923274` |
| 🇷🇺 Russian Federation (RU) | 69 | 24 | 16.2 Mbps | `vpn771768155` |
| 🇹🇭 Thailand (TH) | 29 | 6 | 19.9 Mbps | `vpn416211278` |
| 🇺🇸 United States (US) | 24 | 5 | 4.2 Mbps | `vpn250207254` |
| 🇻🇳 Viet Nam (VN) | 10 | 1 | 14.5 Mbps | `vpn560167748` |
| 🇦🇷 Argentina (AR) | 5 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 5 | 4 | 13.4 Mbps | `vpn863521180` |
| 🇧🇷 Brazil (BR) | 5 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 4 | 2 | 14.7 Mbps | `vpn314968721` |
| 🇮🇩 Indonesia (ID) | 3 | 2 | 16.4 Mbps | `vpn104-cyberdewata` |
| 🇮🇳 India (IN) | 3 | 1 | 11.2 Mbps | `vpn359610091` |
| 🇲🇲 Myanmar (MM) | 3 | 1 | 15.1 Mbps | `vpn477566769` |
| 🇧🇾 Belarus (BY) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 2 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 2 | 0 | 0.0 Mbps | `` |
| 🇬🇧 United Kingdom (GB) | 2 | 0 | 0.0 Mbps | `` |
| 🇭🇰 Hong Kong (HK) | 2 | 1 | 1.1 Mbps | `vpn942711940` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 2 | 0 | 0.0 Mbps | `` |
| 🇲🇽 Mexico (MX) | 2 | 1 | 23.4 Mbps | `vpn678204705` |
| 🇲🇾 Malaysia (MY) | 2 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 2 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇮🇹 Italy (IT) | 1 | 0 | 0.0 Mbps | `` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇳🇱 Netherlands (NL) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇸 Palestinian Territory Occupied (PS) | 1 | 1 | 2.0 Mbps | `vpn921472991` |
| 🇵🇹 Portugal (PT) | 1 | 0 | 0.0 Mbps | `` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |
| 🇻🇪 Venezuela (VE) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn771151831` | 🇰🇷 KR | 43 Mbps | 0.0 Mbps | 0% |
| `vpn406459834` | 🇰🇷 KR | 582 Mbps | 1.6 Mbps | 0% |
| `vpn290308527` | 🇯🇵 JP | 262 Mbps | 0.8 Mbps | 0% |
| `vpn986723868` | 🇯🇵 JP | 223 Mbps | 0.7 Mbps | 0% |
| `vpn779820187` | 🇯🇵 JP | 621 Mbps | 2.2 Mbps | 0% |
| `vpn618946778` | 🇦🇺 AU | 493 Mbps | 2.2 Mbps | 0% |
| `public-vpn-231` | 🇯🇵 JP | 236 Mbps | 1.1 Mbps | 0% |
| `vpn590399715` | 🇷🇺 RU | 20 Mbps | 0.1 Mbps | 1% |
| `vpn942711940` | 🇭🇰 HK | 203 Mbps | 1.1 Mbps | 1% |
| `vpn541474874` | 🇰🇷 KR | 418 Mbps | 2.7 Mbps | 1% |

Most honest of this round: `vpn648203125` (20 Mbps), `vpn501671840` (6 Mbps), `vpn244093263` (18 Mbps), `vpn484776697` (17 Mbps), `vpn757870457` (14 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `vpn921472991` | 🇵🇸 PS | 🇺🇸 US | `172.110.223.66` | 2.0 Mbps |

## 📈 History

Alive % trend (last 21 runs): `██▇▆▆▁▄▅▄▃▄█▄▄▄▄▄▄▃▃▃`

Avg measured speed (Mbps): `▄▅▁▅▁▆▅▄▁▃▁▄▃▄▄▅▅██▄▅`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-11-15 04:20:41 UTC | 90 | 334 | 41% | 12.4 | 29.8 | 0 |
| 2026-11-14 04:17:29 UTC | 98 | 323 | 44% | 11.3 | 54.8 | 2 |
| 2026-11-13 04:22:35 UTC | 97 | 295 | 44% | 14.9 | 46.8 | 1 |
| 2026-11-12 04:23:10 UTC | 93 | 272 | 46% | 15.0 | 29.9 | 0 |
| 2026-11-11 04:22:55 UTC | 97 | 234 | 45% | 12.0 | 28.2 | 0 |
| 2026-11-10 04:16:47 UTC | 95 | 205 | 46% | 12.6 | 65.4 | 1 |
| 2026-11-09 04:26:43 UTC | 93 | 164 | 45% | 11.4 | 39.3 | 0 |
| 2026-11-08 04:18:29 UTC | 97 | 134 | 49% | 11.5 | 47.3 | 1 |
| 2026-11-07 04:14:58 UTC | 93 | 88 | 48% | 10.9 | 27.0 | 1 |
| 2026-11-06 09:50:11 UTC | 96 | 69 | 72% | 11.8 | 26.2 | 0 |
| 2026-10-05 14:10:31 UTC | 95 | 434 | 45% | 8.8 | 52.2 | 4 |
| 2026-10-05 05:01:08 UTC | 94 | 394 | 44% | 10.9 | 50.4 | 3 |
| 2026-10-03 16:01:20 UTC | 98 | 368 | 45% | 8.8 | 33.1 | 4 |
| 2026-10-03 11:25:01 UTC | 99 | 388 | 52% | 11.8 | 37.9 | 5 |
| 2026-10-03 04:45:33 UTC | 94 | 322 | 49% | 12.6 | 77.0 | 5 |

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

All results are in this repo — hotlink them straight from `https://github.com/onlyactions/vpngate-monitor`:

- [`data/latest.json`](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/latest.json) — the merged dataset: every cleaned server + its latest real test result
- [`data/servers_clean.csv`](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/servers_clean.csv) — cleaned, deduplicated server list (no bulky config blobs)
- [`data/summary.json`](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/summary.json) — compact run summary with failure breakdown
- [`data/history.jsonl`](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/history.jsonl) — one JSON line per run, append-only
- [`archive/`](https://github.com/onlyactions/vpngate-monitor/tree/main/archive) — immutable gzipped snapshots of every run
- full logs, raw API response and per-server error details are attached to each [Actions run](https://github.com/onlyactions/vpngate-monitor/actions) as artifacts (30-day retention)

Grab a working VPN right now:

```bash
curl -s https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/latest.json \
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
*Auto-generated by [run #11](https://github.com/onlyactions/vpngate-monitor/actions/runs/43807198337) at 2026-11-16 05:03:17 UTC. Next scheduled run: daily at 03:23 UTC.*
