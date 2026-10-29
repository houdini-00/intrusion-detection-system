from dataclasses import dataclass

@dataclass
class Packet:
    ts: float
    #timestamp: when the packet was seen
    proto: str
    # TCP,UDP,ICMP,ARP
    src: str = ""
    # source IP address
    dst: str = ""
    # destination IP address
    sport: int = 0
    # source port
    dport: int = 0
    # destination port
    flags: str = ""
    # TCP flags such as "S" or "SA"
    payload: bytes = b""
    # the data inside the packet
    icmp_type: int = -1
    # ICMP type (for ICMP packets)
@dataclass
class Alert:
    ts: float
    rule: str        # e.g. "PORT_SCAN"
    severity: str    # "LOW", "MEDIUM", "HIGH" or "CRITICAL"
    src: str
    dst: str
    message: str
    