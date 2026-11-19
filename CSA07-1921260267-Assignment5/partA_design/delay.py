# delay.py
def analyse(packet_bytes=1500, rate_mbps=100, distance_km=2000,
            routers=3, queue_ms=0.5, proc_ms=0.1, speed=2e8):
    bits = packet_bytes * 8
    links = routers + 1
    tx = (bits / (rate_mbps * 1e6)) * 1000 * links        # ms
    prop = (distance_km * 1000 / speed) * 1000            # ms
    queue = routers * queue_ms
    proc = routers * proc_ms
    total = tx + prop + queue + proc
    print(f"Transmission: {tx:.2f} ms | Propagation: {prop:.2f} ms")
    print(f"Queue: {queue:.2f} ms | Processing: {proc:.2f} ms")
    print(f"TOTAL one-way: {total:.2f} ms")
    print(f"Propagation share: {prop/total*100:.1f}%")
    return total

if __name__ == "__main__":
    analyse()