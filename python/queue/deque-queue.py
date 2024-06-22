from collections import deque

class LinkedListQueue:
    """Queue implementation using a singly linked list."""
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self.queue.popleft()
    
    def is_empty(self):
        return self.queue.count() == 0