# 05 - Detection Engine & Rules

This document outlines the design, evaluation strategy, and rule organization of the IDS detection engine.

---

## Detection Approach

The detection engine is designed around two complementary detection mechanisms:

1. **Static Signature Matching**: Evaluating individual packets against known malicious indicators, flag combinations, and payload patterns.
2. **Stateful Behavioral Thresholding**: Tracking aggregate events across a sliding time window (e.g., number of connection attempts to unassigned ports from a single source IP) to identify reconnaissance and flooding behaviors.

---

## Rule & Signature Format Design

Detection rules should be decoupled from the core python engine code, stored in human-readable YAML or JSON files within the `rules/` directory.

### Proposed Rule Schema (Concept)

```yaml
id: "SIG-TCP-001"
name: "TCP Null Scan Detected"
description: "Flags packets arriving with all TCP control flags turned off."
severity: "HIGH"
protocol: "TCP"
conditions:
  flags: [] # No flags set
  direction: "inbound"
alert:
  message: "Potential reconnaissance: TCP NULL scan probe"
  threshold:
    count: 1
    window_seconds: 1
```

```yaml
id: "SIG-HTTP-002"
name: "Suspicious Directory Traversal Attempt"
description: "Detects path traversal sequences in unencrypted HTTP GET/POST payloads."
severity: "MEDIUM"
protocol: "TCP"
dst_port: 80
conditions:
  payload_match:
    type: "regex"
    pattern: "(\.\./|\.\.\\)"
alert:
  message: "Web attack indicator: Directory traversal sequence observed"
```

> [!NOTE]
> [TODO: Update and finalize the official rule syntax once the parser in `src/engine/` is implemented.]

---

## Target Suspicious Behaviors

The initial rule set will target recognizable network attack primitives in controlled test environments:

### 1. Protocol Anomaly & Evasion Signatures
- **NULL Scan**: Packets with zero TCP flags set (`flags == 0`).
- **XMAS Scan**: Packets with FIN, PSH, and URG flags set simultaneously (`flags & 0x29`).
- **SYN-FIN Scan**: Packets with contradictory SYN and FIN flags set at the same time.
- **Large ICMP Echo Requests**: Ping packets exceeding normal MTU/payload thresholds (ping of death / tunneling indicators).

### 2. Behavioral & Heuristic Patterns
- **Port Scan Detection**: A single source IP connecting to more than $N$ unique destination ports within $T$ seconds.
- **SYN Flood / Connection Rate**: A burst of TCP SYN packets from an IP address without completing corresponding 3-way handshakes.

### 3. Application-Level Signatures (Plaintext)
- **Directory Traversal**: Payloads containing `../` or encoded equivalents.
- **Suspicious Shell Spawns**: Payloads containing command execution strings (e.g., `/bin/sh`, `cmd.exe`) in unencrypted traffic.

---

## How Rules Are Organized

To prevent evaluation performance from degrading linearly as rules are added, rules will be organized hierarchically:

```
rules/
├── signatures/
│   ├── network_scans.yaml       # Port scanning, flag anomalies (XMAS, NULL, SYN-FIN)
│   ├── icmp_anomalies.yaml      # Large ping packets, ICMP floods
│   └── web_attacks.yaml         # Directory traversal, basic SQL injection signatures
└── heuristics/
    └── thresholds.yaml          # Rate limits, scan thresholds, window timers
```

### Evaluation Order:
1. **Layer 3 Filter**: Quickly check if packet protocol matches rule (e.g., skip all UDP rules if packet is TCP).
2. **Layer 4 Filter**: Match destination and source port filters.
3. **Flag & Header Evaluation**: Evaluate TCP flags, TTL thresholds, and packet lengths.
4. **Deep Payload Inspection**: Only if all previous checks pass, execute payload substring search or regex matching.

---

## Future Improvements

- [ ] Implement Aho-Corasick or Boyer-Moore multi-pattern string matching algorithms to evaluate all payload signatures in a single pass.
- [ ] Add Snort-rule compatibility layer to ingest open-source threat rules directly.
- [ ] Support dynamic rule reloading without restarting the capture daemon.

---

> Next: [06 - Testing & Validation](06-testing.md)
