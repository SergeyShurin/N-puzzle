from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()
    
    def len(self):
        return len(self.elements)

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        elem = heapq.heappop(self.elements)
        # print("get elem wit priority ", elem[0])
        return elem[1]
    
    def len(self):
        return len(self.elements)
