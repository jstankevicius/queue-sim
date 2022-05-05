import heapq

class PriorityQueue:

    def __init__(self, limit=0):
        self.heap = []
        self.limit = limit
        heapq.heapify(self.heap)

    def head(self):
        return self.heap[0] if not self.empty() else None

    def push(self, e):
        if not self.full():
            heapq.heappush(self.heap, e)

    def pop(self):
        return heapq.heappop(self.heap)

    def size(self):
        return len(self.heap)

    def empty(self):
        return self.size() == 0

    def full(self):
        return self.size() == self.limit and self.limit > 0

