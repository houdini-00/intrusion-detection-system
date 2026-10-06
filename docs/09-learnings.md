# 09 - Lessons Learned & Retrospective

This document captures the technical takeaways, design insights, and reflections gained throughout the project. It covers not just what worked, but also mistakes made, misconceptions corrected, and architectural decisions I would approach differently in the future.

---

## Technical & Networking Takeaways

### Protocol Nuances at the Wire Level
- **Layer Boundaries**: In textbook diagrams, layers appear cleanly separated. In practical packet parsing, variable-length IP options, TCP options (like MSS, SACK, Window Scaling), and padding make byte-offset navigation significantly more error-prone than anticipated.
- **Control Flags**: Observing how scanners (like Nmap) use abnormal flag combinations (NULL, FIN, XMAS) to bypass stateless firewalls clarified why stateful inspection and strict RFC validation are essential.
- **Byte Order (Endianness)**: Working with binary network buffers reinforced the importance of network byte order (Big Endian) versus host byte order (typically Little Endian) when unpacking multibyte integers (ports, IP addresses, sequence numbers).

---

## Security Engineering Takeaways

### The Fragility of Simple Signatures
- Exact string matching on packet payloads is easy to evade using simple techniques: URL encoding, chunked transfer encoding, or splitting keywords across separate TCP segments.
- High-quality rules require strict contextual scoping (e.g., restricting an HTTP regex check specifically to inbound traffic on port 80/8080 with the `PSH/ACK` flags set) rather than naively scanning every byte of every packet.

### False Positives vs. False Negatives
- Security rules are a constant trade-off. An overly aggressive port scan threshold triggers alerts during legitimate administrative tasks or peer-to-peer network discovery, while a lenient threshold lets slow stealth scans pass undetected.

---

## Software Design & Programming Lessons

### Performance in Python
- Python's high-level abstractions provide tremendous speed during prototyping, but single-threaded packet inspection in Python can struggle when network traffic spikes.
- Minimizing memory allocations and avoiding repetitive regex compilation inside per-packet processing loops are critical optimizations.

### Decoupling Rules from Engine Code
- Hardcoding detection logic directly in `if/else` chains quickly becomes unmaintainable. Defining signatures in structured external files (YAML/JSON) makes the engine modular, testable, and maintainable.

---

## Mistakes & What I Would Do Differently

### Early Mistakes
- [TODO: Record design dead-ends or early mistakes as implementation unfolds]

### What I Would Do Differently Next Time
- [TODO: Record architectural approaches that would improve upon the current design]

---

## Summary Assessment

Building an IDS from scratch strips away the mystique of commercial security appliances. Even a simplified prototype exposes the fundamental mechanics of network visibility: you can only protect what you can parse, and you can only detect what you can contextualize.
