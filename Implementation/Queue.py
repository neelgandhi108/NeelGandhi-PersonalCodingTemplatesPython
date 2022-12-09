from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        return self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0