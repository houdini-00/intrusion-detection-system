from collections import defaultdict, deque
from models import Alert


class PortScanDetector:
    def __init__(self, threshold=15, window=10.0):
        self.threshold = threshold
        self.window = window
        # key = (source ip, target ip), value = queue of (timestamp, port)
        self.history = defaultdict(deque)

    def inspect(self, pkt):
        alerts = []

        # only look at "connection start" packets: TCP with just the SYN flag
        if pkt.proto != "TCP" or pkt.flags != "S":
            return alerts

        key = (pkt.src, pkt.dst)
        events = self.history[key]
        events.append((pkt.ts, pkt.dport))

        # TODO 1: remove events older than the window
        while events[0][0] < pkt.ts - self.window:
            events.popleft()

        # TODO 2: count the distinct ports left
        ports = {port for (t, port) in events}

        # TODO 3: raise an alert if the count reaches the threshold
        if len(ports) >= self.threshold:
            alerts.append(Alert(
                ts=pkt.ts,
                rule="PORT_SCAN",
                severity="MEDIUM",
                src=pkt.src,
                dst=pkt.dst,
                message=f"{pkt.src} probed {len(ports)} ports on {pkt.dst}",
            ))

        return alerts