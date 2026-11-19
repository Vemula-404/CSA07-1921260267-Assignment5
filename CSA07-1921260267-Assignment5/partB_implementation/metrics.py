def metrics(trace):
    got = [(s, tx, rx, b) for s, tx, rx, b in trace if rx is not None]
    total, received = len(trace), len(got)
    loss = (total - received) / total * 100
    delays = [rx - tx for s, tx, rx, b in got]
    avg_delay = sum(delays) / len(delays)
    jitter = sum(abs(delays[i+1] - delays[i])
                  for i in range(len(delays) - 1)) / (len(delays) - 1)
    span_ms = got[-1][2] - got[0][1]
    received_bits = sum(b for s, tx, rx, b in got) * 8
    throughput = (received_bits / span_ms) / 1000
    return loss, avg_delay, jitter, throughput

if __name__ == "__main__":
    trace = [(1,0,42,1200),(2,20,61,1200),(3,40,85,1200),(4,60,None,1200),
             (5,80,119,1200),(6,100,146,1200),(7,120,158,1200),
             (8,140,190,1200),(9,160,None,1200),(10,180,222,1200)]
    print("loss=%.1f%% delay=%.1fms jitter=%.1fms thr=%.1fkbps" % metrics(trace))