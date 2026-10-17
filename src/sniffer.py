#TCP three way handshake 
# step 1: SYN (synchronize) - The client sends a SYN packet to the server to initiate a connection.
# step 2: SYN-ACK (synchronize-acknowledge) - The server responds with a SYN-ACK packet to acknowledge the client's request and indicate that it is ready to establish a connection.
# step 3: ACK (acknowledge) - The client sends an ACK packet back to the server to confirm that the connection has been established.

from scapy.all import sniff,IP, TCP

def handle(packet):
    if packet.haslayer(IP):
        print(packet[IP].src, "->", packet[IP].dst)
        if packet.haslayer(TCP):
            print(" ports:",packet[TCP].sport,">",packet[TCP].dport)
            print(" flags:",packet[TCP].flags)

sniff(prn=handle, store=False, count=20)
