#Stacks
Implementation of Stacks with Using Lists

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0
		
Implementation of Stacks with Using collections.deque class

from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0
		
