# 08 - Results & Evidence

This document compiles the empirical results, logs, terminal outputs, and observed performance metrics produced by the intrusion detection system. 

> [!NOTE]
> All metrics and logs documented here are drawn strictly from executed test runs and real capture data. No placeholder metrics or simulated performance numbers are fabricated.

---

## Final Capabilities Summary

> *This checklist reflects confirmed, verified features as they pass lab validation.*

- [ ] Real-time packet capture on live network interface
- [ ] Offline `.pcap` capture playback and evaluation
- [ ] Layer 2, 3, and 4 protocol header decoding
- [ ] Signature matching for malicious TCP flag anomalies
- [ ] Rate-based detection for port scanning activity
- [ ] Payload inspection for unencrypted application attack patterns
- [ ] Structured JSON alert export

---

## Detection Examples & Alert Logs

### Example 1: TCP Port Scan Detection Output
*Awaiting test execution.*

```json
{
  "timestamp": "[TODO: Timestamp]",
  "event": "PORT_SCAN_DETECTED",
  "source_ip": "[TODO: Source IP]",
  "target_ip": "[TODO: Target IP]",
  "scanned_ports_count": 0,
  "time_window_seconds": 0.0,
  "severity": "HIGH"
}
```

### Example 2: Signature Match Alert Output
*Awaiting test execution.*

```text
[TODO: Insert raw console output or alert log format]
```

---

## Visual Evidence

### Terminal Output
> [!NOTE]
> [TODO: Add terminal output screenshot demonstrating IDS running and alerting in `screenshots/`]

### Wireshark Comparison
> [!NOTE]
> [TODO: Add side-by-side screenshot comparing Wireshark packet capture against IDS dissector output]

---

## Measured Performance & Limitations

### Packet Processing Throughput
- **Test Machine Specs**: [TODO: CPU, RAM, OS version]
- **Packet Generation Tool**: [TODO: e.g., `tcpreplay`, Scapy, or test PCAP replay]
- **Observed Throughput**: [TODO: Measured packets per second (pps) before drops occur]
- **Memory Consumption**: [TODO: Peak resident set size (RSS) during active capture]

### Known Detection Gaps
1. **Encrypted Traffic**: Payloads transmitted inside TLS / HTTPS sessions cannot be inspected by this engine.
2. **Out-of-Order Packets**: Because full TCP session reassembly is not yet implemented, signatures split across multiple TCP segments are currently missed.
3. **High-Speed Link Bottlenecks**: As an interpreted Python process running single-threaded dissection, packet drop rates increase significantly on high-throughput interfaces (>100 Mbps).

---

> Next: [09 - Lessons Learned](09-learnings.md)
