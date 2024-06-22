"""Stack implementation."""

class Stack:
    """My representation of a stack as a dictionary.
       It is a last in first out kind of data structure."""
    def __init__(self):
        self.count = 0
        self.items = {}

    def __repr__(self):
        return ''.join(str(self.items)) 

    def push(self, item):
        self.items[self.count] = item
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        poppedItem = self.items.pop(self.count - 1)
        self.count -= 1
        return poppedItem
    
    def is_empty(self):
        return self.count == 0
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.items[self.count - 1]
    
    def clear(self):
        self.items = {}
        self.count = 0

    def size(self):
        return self.count