# 02 - Understanding IDS Fundamentals

Before writing code or selecting libraries, I needed to clearly understand what an Intrusion Detection System actually does and where the real-world engineering trade-offs lie. This document outlines my conceptual breakdown from an engineering perspective rather than a textbook definition.

---

## What an IDS Actually Does

At its simplest, an Intrusion Detection System is an automated observer. It monitors an environment (network traffic, system logs, file integrity), parses events into structured data, compares those events against known threat patterns or statistical deviations, and emits alerts when suspicious activity occurs.

Unlike an antivirus program running on a workstation or a firewall inspecting stateful connection policies, an IDS operates primarily in a passive observation mode. It does not sit in-line by default to block packets; instead, it taps into the stream, inspects the data, and notifies defenders of anomalies.

```
       [ Network Wire / Tap ]
                 │
                 ▼
       [ Packet Capture ]
                 │
                 ▼
       [ Protocol Parsing ]  ---> Drops malformed / unhandled frames
                 │
                 ▼
       [ Detection Engine ]  ---> Evaluates rules against packet headers & payload
                 │
                 ▼
        [ Alert Dispatch ]   ---> Logs alert if conditions match
```

---

## Architectural Distinctions: NIDS vs. HIDS

When deciding what to build, I had to choose between a Network-based IDS (NIDS) and a Host-based IDS (HIDS).

| Dimension | Network-Based IDS (NIDS) | Host-Based IDS (HIDS) |
| :--- | :--- | :--- |
| **Data Source** | Raw network frames / packets captured from a network interface or TAP/SPAN port. | System calls, operating system logs, file modifications, process execution. |
| **Visibility Scope** | Wide network visibility across all communicating endpoints on a monitored subnet. | Deep, granular visibility into a single host's local operations. |
| **Blind Spots** | Encrypted payloads (HTTPS, SSH) hide application content unless terminated/proxied; high link speeds can cause packet drops. | Does not see network traffic destined for other endpoints; adds CPU overhead to the monitored host. |
| **My Decision** | **Selected for this project.** Building a NIDS lets me work directly with network protocols, socket programming, packet headers, and wire-level data. | Deferred to a potential future project. |

---

## Detection Strategies: Signature vs. Anomaly

Modern security systems generally employ two distinct detection models. I evaluated both to determine what was practical for this initial build:

### 1. Signature-Based Detection
- **How it works**: Compares specific attributes of incoming packets against a database of known indicators (e.g., matching a known malicious User-Agent string, specific TCP flag combinations like NULL scans, or known exploit payloads).
- **Pros**: Low computational complexity, deterministic results, low false positive rate for well-crafted rules, easy to write and debug.
- **Cons**: Completely blind to unknown attacks (zero-days) or minor variations designed to evade exact string patterns.

### 2. Anomaly-Based Detection
- **How it works**: Establishes a mathematical baseline of "normal" behavior (e.g., average connection counts, packet sizes, protocol distribution) and alerts when observed traffic significantly deviates from that baseline.
- **Pros**: Capable of detecting previously unseen attacks and subtle exfiltration attempts.
- **Cons**: High false positive rate in dynamic network environments, computationally expensive to maintain sliding-window baselines, and difficult to tune.

### My Approach
I am starting with **signature-based detection** for packet headers and payloads, paired with simple **threshold-based heuristics** (a basic form of behavioral anomaly detection for scenarios like port scanning and connection rate flooding).

---

## Detection vs. Prevention (IDS vs. IPS)

An **Intrusion Detection System (IDS)** is passive:
- Listens on a mirror/promiscuous port or processes offline PCAPs.
- An issue or crash in the detection engine does not take down network connectivity for other devices.
- Fails open: if overwhelmed, it drops packets from inspection, but traffic still reaches destinations.

An **Intrusion Prevention System (IPS)** is inline:
- Sits directly between network segments (like a bridge or firewall).
- Has the authority to drop packets, reset connections (`TCP RST`), or alter firewall tables dynamically.
- Latency introduced by inspection directly degrades network throughput. A bug or bottleneck can break network connectivity entirely.

For this project, building an **IDS** makes the most sense. It allows me to iterate rapidly, test with packet captures safely, and observe packet processing without risking disruption to host networking.

---

## Why Build a Simplified IDS?

Established tools like Suricata, Snort, and Zeek have decades of collective development, SIMD acceleration, and massive rule ecosystems (like Emerging Threats). Rebuilding them from scratch is obviously not about replacing them.

Instead, the motivation is **pedagogical and diagnostic**:
1. When you configure Snort rules in production, understanding how the underlying pattern matcher evaluates packet buffers makes you a significantly better rule author.
2. Handling packet disassembly from raw bytes clarifies exactly why certain TCP evasion techniques (fragmentation overlapping, out-of-order packets) exist and how attackers exploit blind spots.
3. Writing the detection logic exposes the delicate balance between rule precision and resource consumption.

---

> Next: [03 - Architecture & Data Flow](03-architecture.md)
