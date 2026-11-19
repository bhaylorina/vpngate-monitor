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
| **Run** | [#14 · view run](https://github.com/onlyactions/vpngate-monitor/actions/runs/44458235555) · 2026-11-19 04:25:57 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **95** |
| **Duplicates removed** | 0 exact + 1 same-IP |
| **Servers tested** | **1,070 of 1,070** — all 95 current + 975 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **429** — 69 from the current list + 360 historical ♻️ |
| **❌ Dead / unusable** | 641 |
| **Usability** | **72.6%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **11.4 / 12.6 / 47.3 Mbps** |
| **🚀 Fastest verified** | **vpn407625834** · 🇺🇸 United States · **47.3 Mbps** |
| **🧭 Exit-country mismatches** | 3 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.2 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn407625834` | 🇺🇸 United States | 📋 current | `66.114.142.213:1357`/tcp | 2.0s | **47.3 Mbps** | 180.7 Mbps | 1,958,117 |
| 2 | `vpn491348575` | 🇨🇦 Canada | 📋 current | `184.68.30.116:1697`/tcp | 2.3s | **28.8 Mbps** | 22.0 Mbps | 1,238,168 |
| 3 | `vpn888660485` | 🇯🇵 Japan | 📋 current | `219.104.131.96:31969`/udp | 2.5s | **28.5 Mbps** | 976.9 Mbps | 571,326 |
| 4 | `vpn189019752` | 🇯🇵 Japan | ♻️ historical | `131.147.36.66:1195`/udp | 2.5s | **27.9 Mbps** | 932.1 Mbps | 610,142 |
| 5 | `vpn679218486` | 🇯🇵 Japan | ♻️ historical | `124.209.226.195:1752`/udp | 2.5s | **26.3 Mbps** | 682.8 Mbps | 683,399 |
| 6 | `vpn526062445` | 🇯🇵 Japan | ♻️ historical | `60.143.120.123:1632`/udp | 2.5s | **25.0 Mbps** | 538.8 Mbps | 1,465,451 |
| 7 | `vpn772492023` | 🇯🇵 Japan | ♻️ historical | `122.130.236.188:1638`/udp | 2.8s | **23.5 Mbps** | 44.7 Mbps | 1,463,568 |
| 8 | `vpn640114063` | 🇳🇿 New Zealand | 📋 current | `203.109.204.188:1195`/udp | 2.5s | **23.3 Mbps** | 411.6 Mbps | 552,279 |
| 9 | `vpn187938957` | 🇯🇵 Japan | ♻️ historical | `120.75.57.120:1465`/udp | 2.8s | **22.8 Mbps** | 291.0 Mbps | 1,503,825 |
| 10 | `cetsssa` | 🇲🇽 Mexico | ♻️ historical | `189.186.30.193:992`/tcp | 1.8s | **21.6 Mbps** | 53.1 Mbps | 1,368,373 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-100` | 🇯🇵 JP | 3,003,937 | 236.1 Mbps | 2.5 Mbps | 179 | 16.9 d | 2weeks |
| 2 | `public-vpn-258` | 🇯🇵 JP | 2,927,383 | 194.9 Mbps | 13.7 Mbps | 64 | 16.9 d | 2weeks |
| 3 | `public-vpn-78` | 🇯🇵 JP | 2,853,500 | 294.3 Mbps | 11.3 Mbps | 126 | 14.9 d | 2weeks |
| 4 | `public-vpn-206` | 🇯🇵 JP | 2,825,566 | 328.0 Mbps | 0.9 Mbps | 70 | 20.9 d | 2weeks |
| 5 | `public-vpn-39` | 🇯🇵 JP | 2,787,871 | 228.2 Mbps | 11.5 Mbps | 137 | 14.9 d | 2weeks |
| 6 | `public-vpn-71` | 🇯🇵 JP | 2,780,120 | 201.4 Mbps | 3.6 Mbps | 68 | 21.9 d | 2weeks |
| 7 | `public-vpn-95` | 🇯🇵 JP | 2,779,114 | 1,163.6 Mbps | 12.9 Mbps | 256 | 24.9 d | 2weeks |
| 8 | `public-vpn-251` | 🇯🇵 JP | 2,776,080 | 101.8 Mbps | 6.2 Mbps | 92 | 23.9 d | 2weeks |
| 9 | `public-vpn-97` | 🇯🇵 JP | 2,768,299 | 488.5 Mbps | 15.3 Mbps | 115 | 24.9 d | 2weeks |
| 10 | `public-vpn-134` | 🇯🇵 JP | 2,748,495 | 241.4 Mbps | 14.0 Mbps | 56 | 14.9 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 499 | 214 | 28.5 Mbps | `vpn888660485` |
| 🇰🇷 Korea Republic of (KR) | 349 | 168 | 20.3 Mbps | `vpn711923274` |
| 🇷🇺 Russian Federation (RU) | 85 | 19 | 20.6 Mbps | `vpn908098700` |
| 🇹🇭 Thailand (TH) | 37 | 4 | 16.9 Mbps | `vpn620865445` |
| 🇺🇸 United States (US) | 26 | 7 | 47.3 Mbps | `vpn407625834` |
| 🇻🇳 Viet Nam (VN) | 11 | 1 | 2.9 Mbps | `vpn560167748` |
| 🇦🇷 Argentina (AR) | 5 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 5 | 3 | 11.0 Mbps | `vpn759761201` |
| 🇧🇷 Brazil (BR) | 5 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 4 | 1 | 17.3 Mbps | `vpn255850086` |
| 🇮🇩 Indonesia (ID) | 3 | 0 | 0.0 Mbps | `` |
| 🇮🇳 India (IN) | 3 | 1 | 2.8 Mbps | `vpn359610091` |
| 🇲🇲 Myanmar (MM) | 3 | 1 | 14.4 Mbps | `vpn477566769` |
| 🇧🇾 Belarus (BY) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇦 Canada (CA) | 2 | 1 | 28.8 Mbps | `vpn491348575` |
| 🇨🇳 China (CN) | 2 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 2 | 0 | 0.0 Mbps | `` |
| 🇬🇧 United Kingdom (GB) | 2 | 0 | 0.0 Mbps | `` |
| 🇭🇰 Hong Kong (HK) | 2 | 1 | 0.8 Mbps | `vpn942711940` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 2 | 2 | 1.2 Mbps | `vpn457795651` |
| 🇲🇽 Mexico (MX) | 2 | 1 | 21.6 Mbps | `cetsssa` |
| 🇲🇾 Malaysia (MY) | 2 | 0 | 0.0 Mbps | `` |
| 🇳🇿 New Zealand (NZ) | 2 | 2 | 23.3 Mbps | `vpn640114063` |
| 🇵🇭 Philippines (PH) | 2 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 2 | 1 | 0.8 Mbps | `vpn503500791` |
| 🇦🇪 United Arab Emirates (AE) | 1 | 1 | 20.4 Mbps | `vpn196661281` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇮🇹 Italy (IT) | 1 | 0 | 0.0 Mbps | `` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇳🇱 Netherlands (NL) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇦 Panama (PA) | 1 | 1 | 9.1 Mbps | `vpn743273359` |
| 🇵🇸 Palestinian Territory Occupied (PS) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇹 Portugal (PT) | 1 | 0 | 0.0 Mbps | `` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |
| 🇻🇪 Venezuela (VE) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn837693710` | 🇯🇵 JP | 611 Mbps | 0.1 Mbps | 0% |
| `vpn986723868` | 🇯🇵 JP | 223 Mbps | 0.1 Mbps | 0% |
| `public-vpn-37` | 🇯🇵 JP | 1,394 Mbps | 2.7 Mbps | 0% |
| `vpn290308527` | 🇯🇵 JP | 262 Mbps | 0.7 Mbps | 0% |
| `vpn598447077` | 🇯🇵 JP | 97 Mbps | 0.2 Mbps | 0% |
| `public-vpn-206` | 🇯🇵 JP | 328 Mbps | 0.9 Mbps | 0% |
| `vpn110472687` | 🇯🇵 JP | 912 Mbps | 2.9 Mbps | 0% |
| `vpn551090423` | 🇺🇸 US | 94 Mbps | 0.3 Mbps | 0% |
| `vpn517964018` | 🇰🇷 KR | 87 Mbps | 0.3 Mbps | 0% |
| `vpn942711940` | 🇭🇰 HK | 203 Mbps | 0.8 Mbps | 0% |

Most honest of this round: `vpn648203125` (16 Mbps), `vpn501671840` (12 Mbps), `vpn244093263` (15 Mbps), `vpn131652721` (13 Mbps), `vpn940788711` (17 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `vpn196661281` | 🇦🇪 AE | 🇷🇺 RU | `5.228.117.135` | 20.4 Mbps |
| `vpn962496160` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.24` | 1.1 Mbps |
| `vpn457795651` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.20` | 1.2 Mbps |

## 📈 History

Alive % trend (last 24 runs): `██▇▆▆▁▄▅▄▃▄█▄▄▄▄▄▄▃▃▃▃▃▂`

Avg measured speed (Mbps): `▄▅▁▅▁▆▅▄▁▃▁▄▃▄▄▅▅██▄▅█▃▇`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-11-18 04:22:25 UTC | 92 | 389 | 39% | 14.2 | 37.8 | 2 |
| 2026-11-17 04:21:05 UTC | 98 | 397 | 42% | 11.0 | 26.6 | 3 |
| 2026-11-16 04:58:07 UTC | 94 | 366 | 42% | 14.3 | 35.9 | 1 |
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
*Auto-generated by [run #14](https://github.com/onlyactions/vpngate-monitor/actions/runs/44458235555) at 2026-11-19 04:32:37 UTC. Next scheduled run: daily at 03:23 UTC.*
