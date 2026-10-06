# 04 - Implementation Log

This document serves as the chronological engineering journal of the IDS implementation. Each phase and significant technical milestone is recorded using a strict, honest engineering template:

- **What I Wanted to Do**: The specific technical objective for this milestone.
- **Why**: The architectural or security motivation behind this decision.
- **What I Built**: The actual code, modules, or configurations created.
- **How It Works**: High-level explanation of the component's internal logic.
- **What Happened**: What was observed when running or testing the implementation.
- **Problems Encountered**: Unexpected errors, protocol quirks, or edge cases discovered.
- **Next Step**: The logical continuation based on test observations.

---

## Step 0: Repository & Documentation Framework Setup

### What I Wanted to Do
Establish a clean, standardized repository structure and an engineering documentation framework before writing packet processing code.

### Why
Building a security tool without structured tracking leads to undocumented assumptions and unrepeatable testing. Setting up dedicated directories for rules, tests, logs, screenshots, and architecture diagrams ensures every step is reproducible and verifiable.

### What I Built
- Root project structure (`src/`, `rules/`, `tests/`, `screenshots/`, `diagrams/`, `docs/`).
- Initial documentation suite (`01-project-overview.md` through `09-learnings.md`).
- Baseline `.gitignore` to prevent committing capture files (`.pcap`), virtual environments, or compiled bytecode.
- Minimal `requirements.txt` outlining candidate libraries.

### How It Works
The repository is split into distinct responsibilities:
- `src/` holds the executable code.
- `rules/` isolates detection logic from engine code.
- `docs/` functions as an ongoing engineering journal that will be updated alongside each code commit.

### What Happened
Directory structure and baseline documentation created cleanly without unnecessary dependencies or fabricated implementation code.

### Problems Encountered
None at this preliminary stage.

### Next Step
Select the packet ingestion library and build Step 1: the raw packet capture module (evaluating Scapy vs. Python raw sockets).

---

## Step 1: Packet Capture & Ingestion Pipeline

> [!NOTE]
> *Status: Pending Implementation*

### What I Wanted to Do
[TODO: Document the goal for capturing raw packets from interface / PCAP]

### Why
[TODO: Document rationale for capture method choice]

### What I Built
[TODO: Document files created in `src/`]

### How It Works
[TODO: Explain the capture loop, socket configuration, or reader implementation]

### What Happened
[TODO: Document output from running initial capture script]

### Problems Encountered
[TODO: Document permission issues, interface binding errors, or capture drops]

### Next Step
[TODO: Outline dissection layer requirements]

---

## Step 2: Protocol Decapsulation & Layer Dissection

> [!NOTE]
> *Status: Pending Implementation*

### What I Wanted to Do
[TODO: Document goal for parsing Ethernet, IP, TCP, UDP headers]

### Why
[TODO: Document rationale for manual parsing vs. library dissection]

### What I Built
[TODO: Document parser classes and data structures]

### How It Works
[TODO: Explain bitwise shifting, struct unpacking, or object model]

### What Happened
[TODO: Document test results against sample PCAP]

### Problems Encountered
[TODO: Document malformed header handling, padding bytes, or checksum calculation]

### Next Step
[TODO: Outline signature matching engine]

---

## Step 3: Signature & Detection Engine

> [!NOTE]
> *Status: Pending Implementation*

### What I Wanted to Do
[TODO: Document signature matching objectives]

### Why
[TODO: Document rule design choice]

### What I Built
[TODO: Document engine implementation]

### How It Works
[TODO: Explain rule evaluation algorithm]

### What Happened
[TODO: Document matching results against crafted attack packets]

### Problems Encountered
[TODO: Document regex performance overhead or false positives]

### Next Step
[TODO: Outline alerting and logging mechanism]

---

## Step 4: Alerting & Structured Logging

> [!NOTE]
> *Status: Pending Implementation*

### What I Wanted to Do
[TODO: Document alert dispatcher requirements]

### Why
[TODO: Document structured logging format choice]

### What I Built
[TODO: Document logger module]

### How It Works
[TODO: Explain JSON serialization and output streaming]

### What Happened
[TODO: Document log file validation]

### Problems Encountered
[TODO: Document timestamp synchronization or disk I/O bottlenecks]

### Next Step
[TODO: Outline lab testing and validation]

---

> Next: [05 - Detection Engine & Rules](05-detection-engine.md)
