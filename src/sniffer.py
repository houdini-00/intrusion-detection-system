#TCP three way handshake 
# step 1: SYN (synchronize) - The client sends a SYN packet to the server to initiate a connection.
# step 2: SYN-ACK (synchronize-acknowledge) - The server responds with a SYN-ACK packet to acknowledge the client's request and indicate that it is ready to establish a connection.
# step 3: ACK (acknowledge) - The client sends an ACK packet back to the server to confirm that the connection has been established.

from scapy.all import sniff
from converter import from_scapy


def handle(raw):
    pkt = from_scapy(raw)
    if pkt:
        print(pkt)


sniff(prn=handle, store=False, count=20)