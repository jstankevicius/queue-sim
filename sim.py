from priority_queue import PriorityQueue
from worker import Worker
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

TIME = 10
REQS_PER_SEC = 1000
LOADS = list(range(200, 2200, 200))

x = [0]
p50 = [0]
p90 = [0]
p99 = [0]

for load in LOADS:
    # Make a request flow:
    q = PriorityQueue()
    w = Worker()
    latencies = []
    for i in range(TIME * load):
        time = i / load
        q.push(time)

    while not q.empty():
        latencies.append(w.consume(q))


    x.append(load)
    p50.append(np.percentile(latencies, 50))
    p90.append(np.percentile(latencies, 90))
    p99.append(np.percentile(latencies, 99))

    #pprint(latencies)

p50_line, = plt.plot(x, p50)
p90_line, = plt.plot(x, p90)
p99_line, = plt.plot(x, p99)

p50_line.set_label("p50")
p90_line.set_label("p90")
p99_line.set_label("p99")

plt.title("Latency percentiles of simulated worker with infinite queue")
plt.xlabel("Offered load (req/s)")
plt.ylabel("Latency (s)")
plt.tight_layout()

plt.legend()
plt.grid()
plt.show()

