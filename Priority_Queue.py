import heapq

class priority_queue:
    def __init__(self):
        self.queue = []
    def push(self, item, priority):
        heapq.heappush(self.queue,(priority,item))
    def deque(self):
        return heapq.heappop(self.queue)[1]
    def display(self):
        print(str(self.queue))

pq = priority_queue()
pq.push("walking",17)
pq.push("reading",1)
pq.push("running",5)
pq.push("drinking",7)
pq.deque()
pq.display()