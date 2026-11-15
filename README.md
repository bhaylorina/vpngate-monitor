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
| **Run** | [#10 · view run](https://github.com/onlyactions/vpngate-monitor/actions/runs/43676290778) · 2026-11-15 04:20:41 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **90** |
| **Duplicates removed** | 0 exact + 1 same-IP |
| **Servers tested** | **810 of 810** — all 90 current + 720 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **334** — 56 from the current list + 278 historical ♻️ |
| **❌ Dead / unusable** | 476 |
| **Usability** | **62.2%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **12.4 / 13.6 / 29.8 Mbps** |
| **🚀 Fastest verified** | **vpn399531613** · 🇯🇵 Japan · **29.8 Mbps** |
| **🧭 Exit-country mismatches** | 0 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 2.8 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn399531613` | 🇯🇵 Japan | ♻️ historical | `60.109.2.15:1354`/udp | 1.8s | **29.8 Mbps** | 502.7 Mbps | 689,162 |
| 2 | `vpn526062445` | 🇯🇵 Japan | ♻️ historical | `60.143.120.123:1632`/udp | 1.8s | **29.7 Mbps** | 538.8 Mbps | 1,465,451 |
| 3 | `vpn649976307` | 🇯🇵 Japan | 📋 current | `163.58.83.64:1822`/udp | 2.0s | **29.1 Mbps** | 319.8 Mbps | 586,080 |
| 4 | `vpn367633262` | 🇯🇵 Japan | ♻️ historical | `138.64.87.141:39975`/udp | 1.8s | **28.1 Mbps** | 665.7 Mbps | 670,751 |
| 5 | `cetsssa` | 🇲🇽 Mexico | ♻️ historical | `189.186.30.193:992`/tcp | 2.3s | **27.3 Mbps** | 59.3 Mbps | 1,119,112 |
| 6 | `vpn909153861` | 🇯🇵 Japan | ♻️ historical | `138.64.96.118:14355`/udp | 2.3s | **26.5 Mbps** | 194.2 Mbps | 812,170 |
| 7 | `vpn759611927` | 🇯🇵 Japan | 📋 current | `61.114.197.133:1371`/udp | 2.0s | **24.1 Mbps** | 191.2 Mbps | 1,259,804 |
| 8 | `vpn644907313` | 🇯🇵 Japan | ♻️ historical | `126.125.123.228:1401`/udp | 2.0s | **22.7 Mbps** | 93.7 Mbps | 1,107,252 |
| 9 | `vpn754234555` | 🇰🇷 Korea Republic of | 📋 current | `58.120.113.176:1288`/tcp | 2.3s | **22.2 Mbps** | 306.5 Mbps | 1,326,248 |
| 10 | `vpn678204705` | 🇲🇽 Mexico | ♻️ historical | `189.219.64.67:1195`/udp | 1.8s | **22.2 Mbps** | 96.5 Mbps | 616,667 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-100` | 🇯🇵 JP | 3,003,937 | 236.1 Mbps | 15.5 Mbps | 179 | 16.9 d | 2weeks |
| 2 | `public-vpn-258` | 🇯🇵 JP | 2,927,383 | 194.9 Mbps | 13.4 Mbps | 64 | 16.9 d | 2weeks |
| 3 | `public-vpn-154` | 🇯🇵 JP | 2,864,520 | 208.0 Mbps | 11.7 Mbps | 104 | 19.9 d | 2weeks |
| 4 | `public-vpn-200` | 🇯🇵 JP | 2,846,412 | 177.2 Mbps | 12.0 Mbps | 51 | 18.9 d | 2weeks |
| 5 | `public-vpn-160` | 🇯🇵 JP | 2,839,108 | 217.2 Mbps | 17.6 Mbps | 120 | 21.9 d | 2weeks |
| 6 | `public-vpn-185` | 🇯🇵 JP | 2,833,369 | 238.2 Mbps | 8.3 Mbps | 121 | 21.9 d | 2weeks |
| 7 | `public-vpn-206` | 🇯🇵 JP | 2,825,566 | 328.0 Mbps | 0.9 Mbps | 70 | 20.9 d | 2weeks |
| 8 | `public-vpn-39` | 🇯🇵 JP | 2,787,871 | 228.2 Mbps | 15.0 Mbps | 137 | 14.9 d | 2weeks |
| 9 | `public-vpn-67` | 🇯🇵 JP | 2,767,567 | 303.6 Mbps | 8.0 Mbps | 58 | 19.9 d | 2weeks |
| 10 | `public-vpn-134` | 🇯🇵 JP | 2,748,495 | 241.4 Mbps | 10.1 Mbps | 56 | 14.9 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 375 | 179 | 29.8 Mbps | `vpn399531613` |
| 🇰🇷 Korea Republic of (KR) | 268 | 115 | 22.2 Mbps | `vpn754234555` |
| 🇷🇺 Russian Federation (RU) | 61 | 18 | 18.5 Mbps | `vpn908098700` |
| 🇹🇭 Thailand (TH) | 27 | 6 | 18.0 Mbps | `vpn612027927` |
| 🇺🇸 United States (US) | 22 | 6 | 13.6 Mbps | `vpn621884204` |
| 🇻🇳 Viet Nam (VN) | 9 | 1 | 1.0 Mbps | `vpn560167748` |
| 🇧🇷 Brazil (BR) | 5 | 0 | 0.0 Mbps | `` |
| 🇦🇷 Argentina (AR) | 4 | 1 | 10.9 Mbps | `vpn475984108` |
| 🇦🇺 Australia (AU) | 4 | 2 | 9.1 Mbps | `vpn164471586` |
| 🇮🇳 India (IN) | 3 | 1 | 2.5 Mbps | `vpn359610091` |
| 🇲🇲 Myanmar (MM) | 3 | 0 | 0.0 Mbps | `` |
| 🇧🇾 Belarus (BY) | 2 | 0 | 0.0 Mbps | `` |
| 🇬🇧 United Kingdom (GB) | 2 | 0 | 0.0 Mbps | `` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 2 | 0 | 0.0 Mbps | `` |
| 🇮🇩 Indonesia (ID) | 2 | 1 | 7.2 Mbps | `vpn797871879` |
| 🇲🇽 Mexico (MX) | 2 | 2 | 27.3 Mbps | `cetsssa` |
| 🇲🇾 Malaysia (MY) | 2 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 2 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 2 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 1 | 1 | 8.9 Mbps | `_unregistered_vpn859862680` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 1 | 0 | 0.0 Mbps | `` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇭🇰 Hong Kong (HK) | 1 | 0 | 0.0 Mbps | `` |
| 🇮🇹 Italy (IT) | 1 | 0 | 0.0 Mbps | `` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇳🇱 Netherlands (NL) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇹 Portugal (PT) | 1 | 1 | 21.7 Mbps | `vpn407307981` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |
| 🇻🇪 Venezuela (VE) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn184169581` | 🇯🇵 JP | 701 Mbps | 0.5 Mbps | 0% |
| `vpn771151831` | 🇰🇷 KR | 43 Mbps | 0.1 Mbps | 0% |
| `vpn569352061` | 🇯🇵 JP | 632 Mbps | 1.2 Mbps | 0% |
| `public-vpn-206` | 🇯🇵 JP | 328 Mbps | 0.9 Mbps | 0% |
| `vpn844843933` | 🇯🇵 JP | 118 Mbps | 0.3 Mbps | 0% |
| `vpn486662942` | 🇯🇵 JP | 323 Mbps | 2.1 Mbps | 1% |
| `vpn598447077` | 🇯🇵 JP | 97 Mbps | 0.7 Mbps | 1% |
| `public-vpn-257` | 🇯🇵 JP | 317 Mbps | 2.2 Mbps | 1% |
| `vpn986723868` | 🇯🇵 JP | 223 Mbps | 1.8 Mbps | 1% |
| `vpn359610091` | 🇮🇳 IN | 308 Mbps | 2.5 Mbps | 1% |

Most honest of this round: `vpn501671840` (14 Mbps), `vpn757870457` (13 Mbps), `vpn244093263` (16 Mbps), `vpn131652721` (12 Mbps), `vpn408435278` (13 Mbps).

## 🧭 Exit-country mismatches

. ✅ Every verified server exits where it claims.

## 📈 History

Alive % trend (last 20 runs): `██▇▆▆▁▄▅▄▃▄█▄▄▄▄▄▄▃▃`

Avg measured speed (Mbps): `▄▅▁▅▁▆▅▄▁▃▁▄▃▄▄▅▅██▄`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
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
| 2026-10-02 22:01:53 UTC | 97 | 164 | 28% | 12.9 | 97.8 | 5 |

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
*Auto-generated by [run #10](https://github.com/onlyactions/vpngate-monitor/actions/runs/43676290778) at 2026-11-15 04:25:31 UTC. Next scheduled run: daily at 03:23 UTC.*
