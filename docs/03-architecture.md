# 03 - Architecture & Data Flow

This document details the architectural design of the intrusion detection system, covering component boundaries, data flow pipelines, packet decapsulation mechanics, and alert propagation.

---

## High-Level Architecture Overview

The system follows a sequential pipeline design where each packet moves through ingestion, normalization/decapsulation, rule matching, and reporting stages.

```
       +---------------------------------------------+
       |            Packet Source                    |
       |  (Live Network Interface / Offline PCAP)   |
       +---------------------------------------------+
                              │
                              ▼
       +---------------------------------------------+
       |          Packet Ingestion Module            |
       |  (Raw socket reader / PCAP stream handler)  |
       +---------------------------------------------+
                              │ [Raw Bytes / Layer 2 Frame]
                              ▼
       +---------------------------------------------+
       |         Packet Parser & Dissector           |
       |  (Decodes Ethernet -> IP -> TCP/UDP/ICMP)   |
       +---------------------------------------------+
                              │ [Structured Packet Object]
                              ▼
       +---------------------------------------------+
       |             Detection Engine                |
       |  - Signature Matcher (Header & Payload)     |
       |  - Heuristic Engine (Threshold & Rates)     |
       +---------------------------------------------+
                              │ [Alert Event]
                              ▼
       +---------------------------------------------+
       |          Alerting & Logging Module          |
       |  (Console display, JSON log file, metrics)  |
       +---------------------------------------------+
```

> [!NOTE]
> [TODO: Add architecture diagram generated from draw.io / Mermaid as an image asset in `diagrams/`.]

---

## Core System Components

### 1. Ingestion Layer (`src/capture/`)
- **Responsibility**: Interface with either the host's network adapter in promiscuous mode or read packets sequentially from standard `.pcap` files.
- **Input**: Physical network wire, virtual interface, or binary capture file.
- **Output**: Raw packet byte-arrays paired with metadata (timestamp, wire length, interface index).

### 2. Dissection Layer (`src/parser/`)
- **Responsibility**: Decode raw byte streams into structured, queryable data classes.
- **Layer 2 (Data Link)**: Strips Ethernet framing, checks EtherType (IPv4 vs. IPv6 vs. ARP).
- **Layer 3 (Network)**: Validates IP checksum, extracts Source IP, Destination IP, TTL, Protocol ID, and handles IP options.
- **Layer 4 (Transport)**: Unpacks TCP/UDP/ICMP headers. For TCP, extracts source/destination ports, sequence/acknowledgment numbers, data offset, and control flags (SYN, ACK, FIN, RST, PSH, URG).
- **Layer 7 (Application / Payload)**: Extracts residual payload bytes for pattern and regex matching.

### 3. Detection Engine (`src/engine/`)
- **Responsibility**: Compare parsed packet objects against active rule definitions.
- **Components**:
  - **Rule Evaluator**: Executes fast checks first (Protocol -> Ports -> IP ranges) before proceeding to expensive checks (regex / substring searches in payloads).
  - **State / Tracker Cache**: Maintains in-memory sliding windows (e.g., source IP to unique destination ports accessed within a time window) to spot port scans and sweep activity.

### 4. Alert & Output Manager (`src/alerts/`)
- **Responsibility**: Format and dispatch confirmed alerts to configured sinks.
- **Output Formats**:
  - Standard output console with severity colorization.
  - Append-only structured JSON log file (`alerts.json`) for machine parsing and SIEM ingestion.

---

## Detailed Data Flow: From Wire to Alert

1. **Packet Capture**: The capture worker captures an Ethernet frame.
2. **Sanity Check**: Frames smaller than the minimum header size (14 bytes for standard Ethernet) are dropped.
3. **Layer Traversal**:
   - If EtherType is `0x0800` (IPv4), the packet is passed to the IPv4 dissector.
   - If Protocol is `6` (TCP), the packet is passed to the TCP dissector.
4. **Context Construction**: A `PacketContext` object is constructed containing:
   ```json
   {
     "timestamp": "2026-10-06T12:00:01.123456Z",
     "src_ip": "192.168.1.105",
     "dst_ip": "192.168.1.1",
     "protocol": "TCP",
     "src_port": 49152,
     "dst_port": 22,
     "flags": ["SYN"],
     "payload_length": 0,
     "payload": ""
   }
   ```
5. **Rule Matching**: The `PacketContext` is evaluated against loaded rules sequentially or via indexed lookup tables (e.g., indexed by destination port or protocol).
6. **Alert Emission**: If a rule matches:
   - Severity and rule ID are assigned.
   - Alert object is written to disk and displayed on the terminal.

---

## Future Architecture Improvements

As the system matures, the architecture can expand to address known limitations:
- **Zero-Copy Processing**: Utilizing memory-mapped buffers (`AF_PACKET` on Linux) to prevent excessive memory allocations during high traffic.
- **Multi-Threaded / Worker Queues**: Decoupling packet ingestion from rule evaluation using a thread-safe queue or multiprocessing queue to minimize dropped packets.
- **Stateful Flow Table**: Tracking bidirectional connections (TCP 3-way handshake, sequence tracking) to assemble fragmented packets and unsegmented payloads before inspection.

---

> Next: [04 - Implementation Log](04-implementation.md)
