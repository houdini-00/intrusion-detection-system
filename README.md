# Building an Intrusion Detection System From Scratch

A hands-on engineering project documenting the design, implementation, and evaluation of a lightweight network intrusion detection system (IDS) built from the ground up. This repository functions as both a working cybersecurity tool and a technical project journal detailing technical trade-offs, packet analysis experiments, and debugging lessons.

---

## Why I Built This

Most cybersecurity practitioners interact with intrusion detection systems (such as Snort, Suricata, or Zeek) as pre-packaged appliances or black boxes: traffic flows in, rules are matched, and alerts appear on a dashboard. 

I wanted to peel back that abstraction. I wanted to understand the mechanical reality of what actually happens between raw network frames hitting a network interface card and an alert firing. By building a simplified IDS from scratch, I can observe firsthand the computational challenges of packet inspection, the nuances of protocol decapsulation, state tracking, and the practical difficulties of balancing detection accuracy against false positives.

## Project Goals

- **Deconstruct packet analysis**: Gain a low-level understanding of how raw packets are captured, parsed across network layers (Ethernet, IP, TCP/UDP/ICMP), and prepared for inspection.
- **Implement a modular detection engine**: Build a rule evaluation system capable of signature-based pattern matching and basic behavioral thresholding.
- **Produce actionable alerts**: Generate structured logs and security alerts containing relevant context (timestamp, source/destination IPs and ports, signature match details).
- **Maintain an honest engineering journal**: Document the genuine development process—including implementation roadblocks, false assumptions, bug investigations, and lessons learned.
- **Validate with controlled testing**: Verify detection efficacy against benign baseline traffic and deliberate, controlled security test scenarios within an isolated lab environment.

## Planned Architecture

The planned system operates as a pipeline: packet capture/ingestion, packet dissection, detection engine evaluation, and structured alert output.

```
+--------------------+      +--------------------+      +----------------------+      +--------------------+
|  Network Traffic   | ---> | Packet Ingestion   | ---> | Detection Engine     | ---> | Alerting & Logging |
|  (Live / PCAP)     |      | & Layer Dissection |      | (Signatures & Rules) |      | (Console / JSON)   |
+--------------------+      +--------------------+      +----------------------+      +--------------------+
```

> [!NOTE]
> [TODO: Add detailed architecture diagram as the design solidifies in `diagrams/`.]

For an in-depth breakdown of the system components and data flow, see [03-architecture.md](docs/03-architecture.md).

## Technology Stack

> *Note: Technologies listed below are candidates under active evaluation. This section will be updated as implementation choices are tested and finalized.*

| Component | Candidate Technology | Rationale / Consideration |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Rapid prototyping, extensive networking ecosystem, readability |
| **Packet Ingestion** | Scapy / Raw Sockets / PyShark | Trade-off between high-level protocol parsing ease vs. low-level packet processing throughput |
| **Rule Specification** | YAML / JSON | Human-readable, structured format for defining signature sets |
| **Testing Framework** | `pytest` + Scapy packet replay | Repeatable unit testing of dissection logic and rule triggers |
| **Environment** | Linux / Windows Lab (Isolated) | Safe containment for packet replay and port scan simulations |

## Current Progress

- [x] Project planning & documentation framework
- [ ] Environment setup & dependency selection
- [ ] Network traffic collection (live capture & PCAP parsing)
- [ ] Traffic analysis & protocol dissection
- [ ] Detection logic & signature matching
- [ ] Alert generation & formatting
- [ ] Structured logging
- [ ] Controlled testing & validation
- [ ] Complete technical documentation
- [ ] Final improvements & performance review

## Project Documentation

This project is documented as a living technical journal across 9 dedicated chapters:

1. [01 - Project Overview](docs/01-project-overview.md): Core problem statement, motivation, scope boundaries, and development methodology.
2. [02 - Understanding IDS Fundamentals](docs/02-understanding-ids.md): Practical breakdown of NIDS vs. HIDS, signature vs. anomaly detection, and IDS vs. IPS trade-offs.
3. [03 - Architecture & Data Flow](docs/03-architecture.md): Component breakdown, packet pipeline, and state flow from network wire to alert.
4. [04 - Implementation Log](docs/04-implementation.md): Chronological record of development steps (What I Wanted to Do, Why, What I Built, What Happened).
5. [05 - Detection Engine & Rules](docs/05-detection-engine.md): Signature formats, behavioral detection logic, rule organization, and alert criteria.
6. [06 - Testing & Validation](docs/06-testing.md): Methodology for testing against normal baseline traffic and simulated attacks in an isolated lab.
7. [07 - Troubleshooting & Root Cause Analysis](docs/07-troubleshooting.md): Structured post-mortems of real bugs, wrong assumptions, investigations, and fixes.
8. [08 - Results & Evidence](docs/08-results.md): Real capture examples, terminal outputs, alert logs, and observed performance limitations.
9. [09 - Lessons Learned](docs/09-learnings.md): Technical takeaways across networking, security engineering, software design, and debugging.

## Project Structure

```text
intrusion-detection-system/
├── README.md                 # Project overview, goals, stack, and progress
├── requirements.txt          # Python dependencies
├── LICENSE                   # Open-source license (MIT)
├── docs/                     # Technical project journal & architectural documentation
│   ├── 01-project-overview.md
│   ├── 02-understanding-ids.md
│   ├── 03-architecture.md
│   ├── 04-implementation.md
│   ├── 05-detection-engine.md
│   ├── 06-testing.md
│   ├── 07-troubleshooting.md
│   ├── 08-results.md
│   └── 09-learnings.md
├── src/                      # Core IDS implementation source code
├── rules/                    # Detection rules, signatures, and configuration files
├── tests/                    # Unit tests, mock packet fixtures, and validation scripts
├── screenshots/              # Terminal capture logs, Wireshark traces, and alert proof
└── diagrams/                 # Architecture, flowcharts, and protocol state diagrams
```

## Results

> [!NOTE]
> [TODO: Add final detection results, log snippets, and measured metrics once implementation and lab testing are complete. See `docs/08-results.md` for ongoing observations.]

## Future Improvements

- [ ] Support multi-packet state tracking (TCP stream reassembly)
- [ ] Benchmark packet processing overhead under elevated traffic rates
- [ ] Export alerts to standardized SIEM formats (CEF / JSON / Syslog)
- [ ] Implement signature hot-reloading without restarting capture processes

## Disclaimer

All security testing, traffic generation, and packet inspection documented in this repository are performed strictly within private, isolated lab environments, dedicated virtual machines, or local loopback networks that I own and have explicit authorization to test. No techniques or tools in this project are intended or used against unauthorized networks or third-party targets.
