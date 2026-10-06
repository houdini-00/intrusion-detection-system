# 01 - Project Overview

## What This Project Is

This repository documents the development of a lightweight, custom-built Network Intrusion Detection System (NIDS) written from scratch in Python. Rather than serving as an academic essay or a production-ready alternative to established tools like Snort or Zeek, this project is an active engineering journey. It follows the process of building, dissecting, testing, and debugging a network defense tool at the packet level.

## Why I Decided to Build It

In many cybersecurity courses and labs, network monitoring is introduced through existing user interfaces or pre-configured appliances. You run an Nmap scan, look at a security dashboard, and observe a rule triggering an alert.

However, treating security monitoring tools as opaque black boxes hides the most interesting engineering questions:
- How does raw binary data off a network interface card become a structured packet object?
- What performance trade-offs occur when examining every packet header versus inspecting the payload content?
- How does detection logic actually correlate separate packets into a single behavioral detection (like a port scan)?
- What causes benign traffic to trigger false positives, and how can rules be refined without missing genuine threats?

I wanted to bridge the gap between theory and code. Building a simplified system myself forces me to confront packet decapsulation, protocol nuances, edge cases, and parser bottlenecks directly.

## The Problem I Want to Solve

Defenders face two persistent challenges when inspecting network traffic:
1. **Visibility without overwhelming overhead**: Inspecting network traffic requires extracting key metadata (IP addresses, protocol flags, ports, payload snippets) fast enough to keep up with network flow without dropping packets.
2. **Signal-to-noise ratio**: Simple detection rules often trigger on benign network anomalies, while overly strict rules miss variations of malicious activity.

Through this project, I want to explore how a minimal detection engine handles these problems, examining where basic signature matching succeeds and where its architectural limitations begin to show.

## Initial Goals

- [ ] **Packet Ingestion Pipeline**: Ingest packets from both saved packet capture files (`.pcap`) and live network interfaces.
- [ ] **Multi-Layer Protocol Decoding**: Parse foundational network headers across Layer 2 (Ethernet), Layer 3 (IPv4/IPv6), and Layer 4 (TCP, UDP, ICMP).
- [ ] **Signature & Rule Parser**: Design an intuitive rule definition schema that supports filtering by protocol, IP address range, port numbers, flags, and payload string/regex matches.
- [ ] **Behavioral Detection (Heuristics)**: Implement detection for high-frequency patterns, such as TCP SYN port scans or ICMP floods.
- [ ] **Alert Logging & Reporting**: Emit structured alert logs containing the offending packet's context for downstream analysis.
- [ ] **Transparent Engineering Log**: Record every failure, wrong assumption, bug, and fix across the `docs/` journal.

## Scope and Boundaries

To keep the project focused, achievable, and educational, I have defined strict boundaries:

### In Scope
- Offline PCAP replay and controlled live capture on dedicated test interfaces.
- Decoding IPv4, TCP, UDP, and ICMP protocols.
- Basic payload string and regex pattern matching.
- Simple connection state tracking and frequency thresholding (e.g., scan detection).
- File-based structured logging (JSON / structured text).

### Out of Scope (For Initial Phases)
- Full TCP stream reassembly or session defragmentation (handled in future iterations).
- Decryption of TLS/HTTPS encrypted traffic (detection will focus on metadata, SNI, or unencrypted protocols).
- Multi-gigabit enterprise throughput optimization.
- Active packet dropping or firewall manipulation (this is strictly an *Intrusion Detection System*, not an *Intrusion Prevention System*).
- Complex machine learning or neural anomaly detection models.

---

> Next: [02 - Understanding IDS Fundamentals](02-understanding-ids.md)
