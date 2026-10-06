# 06 - Testing & Validation

Testing an intrusion detection system requires validating two distinct scenarios:
1. **Benign baseline traffic**: Ensuring normal network traffic flows through the parser without triggering false alerts or crashing the engine.
2. **Controlled malicious/simulated traffic**: Confirming that specific attack primitives reliably trigger the appropriate detection rules.

---

## Testing Methodology

To guarantee safety and repeatability:
- All live tests are performed exclusively within an isolated virtual lab environment or against local loopback interfaces (`127.0.0.1` / host-only virtual network).
- Offline tests are conducted using reproducible packet capture (`.pcap`) files containing recorded benign or test traffic.
- Every test is structured with predefined inputs, expected outcomes, and observed behaviors.

---

## Test Scenarios Matrix

| Test ID | Category | Description | Tool / Traffic Source | Expected Alert | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TEST-01** | Baseline | Normal HTTP/HTTPS web browsing | Browser / `curl` | No alerts triggered | Pending |
| **TEST-02** | Baseline | Standard DNS resolution requests | `nslookup` / `dig` | No alerts triggered | Pending |
| **TEST-03** | Malicious | TCP NULL Scan (`-sN`) | Nmap / Scapy script | `SIG-TCP-001` (Null Scan) | Pending |
| **TEST-04** | Malicious | TCP XMAS Scan (`-sX`) | Nmap / Scapy script | `SIG-TCP-002` (XMAS Scan) | Pending |
| **TEST-05** | Malicious | Rapid TCP Port Scan (top 100 ports) | Nmap / Python socket loop | `HEUR-PORT-SCAN` (Threshold exceeded) | Pending |
| **TEST-06** | Malicious | Plaintext Directory Traversal | `curl` with `../../etc/passwd` | `SIG-HTTP-002` (Path Traversal) | Pending |

---

## Detailed Test Logs

### Test Run: TEST-01 - Baseline Web Browsing
- **Date**: [TODO: Date executed]
- **Environment**: [TODO: Host OS, interface details]
- **Input Data**: [TODO: Replayed PCAP / Live capture]
- **Expected Outcome**: Engine parses 100% of packets without unhandled exceptions; zero false positives.
- **Actual Outcome**: [TODO: Record results once test is run]
- **Observations / Log Output**:
  ```text
  [TODO: Paste log snippet here]
  ```

---

### Test Run: TEST-03 - TCP NULL Scan Detection
- **Date**: [TODO: Date executed]
- **Environment**: Isolated lab network
- **Command Executed**:
  ```bash
  # Executed strictly in isolated lab environment:
  nmap -sN -p 80,443,22 192.168.x.x
  ```
- **Expected Outcome**: Trigger `SIG-TCP-001` for each target port with flags `0x00`.
- **Actual Outcome**: [TODO: Record results once test is run]
- **Evidence / Screenshot**:
  > [!NOTE]
  > [TODO: Add screenshot of alert terminal or Wireshark trace in `screenshots/` and link here.]

---

## Identified Limitations & Edge Cases

Documenting where the system currently fails or produces unexpected results:

1. **Packet Dropping Under Load**:
   - [TODO: Record threshold at which python parser begins dropping packets during high-speed traffic].
2. **False Positives**:
   - [TODO: Document any benign applications that triggered unexpected signature matches].
3. **Fragmentation Evasion**:
   - [TODO: Note how engine behaves when signatures are split across IP packet fragments].

---

> Next: [07 - Troubleshooting & Root Cause Analysis](07-troubleshooting.md)
