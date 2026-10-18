from scapy.all import IP, TCP, UDP, ICMP
from converter import from_scapy

fake_tcp = IP(src="10.0.0.5", dst="10.0.0.80") / TCP(sport=40000, dport=80, flags="S")
fake_udp = IP(src="10.0.0.5", dst="8.8.8.8") / UDP(sport=5000, dport=53)
fake_icmp = IP(src="10.0.0.5", dst="10.0.0.1") / ICMP(type=8)

for raw in (fake_tcp, fake_udp, fake_icmp):
    print(from_scapy(raw))