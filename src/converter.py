from scapy.all import IP,TCP,UDP,ICMP
from models import Packet

def from_scapy(raw):
    """turn a scapy packet into a packet
    into our packet.return none if we don't care about it"""
    if not raw.haslayer(IP):
        return None
    ip  = raw[IP]
    if raw.haslayer(TCP):
        tcp = raw[TCP]
        return Packet(
            ts=float(raw.time),
            proto = "TCP",
            src = ip.src,
            dst = ip.dst,
            sport = int(tcp.sport),
            dport = int(tcp.dport),
            flags = str(tcp.flags),
            payload = bytes(tcp.payload)
        )
    if raw.haslayer(UDP):
        udp = raw[UDP]
        return Packet(
            ts=float(raw.time),
            proto = "UDP",
            src = ip.src,
            dst = ip.dst,
            sport = int(udp.sport),
            dport = int(udp.dport),
            payload = bytes(udp.payload)
        )

    if raw.haslayer(ICMP):
        icmp = raw[ICMP]
        return Packet(
            ts=float(raw.time),
            proto = "ICMP",
            src = ip.src,
            dst = ip.dst,
            icmp_type  = int(icmp.type),
        )

    