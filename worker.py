from priority_queue import PriorityQueue
import numpy as np
import yaml
import random

class Worker:
    
    def __init__(self, queue_size=0):
        self.total_delay = 0
        self.worker_queue = PriorityQueue(limit=queue_size)

        with open("latency_samples.yaml") as f:
            self.dist = yaml.full_load(f)["latencies"]

    def consume(self, work_queue: PriorityQueue):
        if not work_queue.empty():
            event_time = work_queue.pop()
            processing_delay  = random.choice(self.dist)

            # Have to incorporate current delay:
            completion_time = event_time + self.total_delay + processing_delay

            # Get next event:
            if not work_queue.empty():
                next_event_time = work_queue.head()
                self.total_delay = max(completion_time - next_event_time, 0)

            # Return this request's latency:
            #print(completion_time - event_time)
            return completion_time - event_time