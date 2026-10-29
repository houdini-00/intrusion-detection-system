from models import Packet
from detectors import PortScanDetector

det = PortScanDetector()

def syn(src, dst, port, t):
    return Packet(ts=t, proto="TCP", src=src, dst=dst, dport=port, flags="S")

print("--- normal browsing: same port, many times ---")
for i in range(30):
    print(det.inspect(syn("10.0.0.5", "10.0.0.80", 443, i * 0.1)))

print("--- scan: 30 different ports quickly ---")
for port in range(1, 31):
    result = det.inspect(syn("10.0.0.66", "10.0.0.10", port, port * 0.1))
    if result:
        print(port, result)
        print("--- slow scan: one port per minute should NOT alert ---")
det2 = PortScanDetector()
for port in range(1, 31):
    result = det2.inspect(syn("10.0.0.77", "10.0.0.10", port, port * 60))
    if result:
        print("UNEXPECTED ALERT", result)
print("done")