"""Queue implementation."""

class Queue:
    """My representation of a queue as a dictionary.
       It is a first in first out kind of data structure."""
    def __init__(self):
        self.count = 0
        self.lowest_count = 0
        self.items = {}

    def __repr__(self):
          return ''.join(str(self.items))
    
    def enqueue(self, item):
        self.items[self.count] = item
        self.count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        popped_item = self.items.pop(self.lowest_count)
        self.lowest_count += 1
        return popped_item

    def is_empty(self):
         return self.count == 0
