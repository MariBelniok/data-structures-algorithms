class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    """Python implementation of a singly linked list."""

    def __init__(self, nodes=None):
        """Initialize the linked list."""
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self) -> str:
        """Return a string representation of the linked list."""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return " -> ".join(str(nodes))

    def __iter__(self):
        """Transverse the linked list."""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_front(self, node):
        """Add a node to the front of the list. Time complexity: O(1)."""
        node.next = self.head # Assign the next of the new head to the current head
        self.head = node # Set the head to the new node
    
    def add_back(self, node):
        """Add a node to the back of the list. Time complexity: O(n)."""
        if self.head is None:
            self.head = node
            return
        for current_node in self: # skip to next if current_node exists
            pass
        current_node.next = node

    def add_after(self, target_node, new_node):
        """Add a node after the target node. Time complexity: O(n)."""
        if self.head is None:
            raise Exception("Cannot add node to empty list.")
        
        for node in self:
            if node.data == target_node:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception("Target node not found.")
    
    def add_before(self, target_node, new_node):
        """Add a node before the target node. Time complexity: O(n)."""
        if self.head is None:
            raise Exception("Cannot add node to empty list.")
        
        if self.head.data == target_node:
            return self.add_front(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Target node not found.")
    
    def remove_node(self, target_node):
        """Remove the first node with the target data. Time complexity: O(n)."""
        if self.head is None:
            raise Exception("Cannot remove node from empty list.")
        
        if self.head.data == target_node:
            self.head = self.head.next
            return
        
        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = node.next
                return
            prev_node = node
            
        raise Exception("Target node not found.")
    
    def reverse(self):
        """Reverse the linked list. Time complexity: O(1)."""
       
        prev, temp = None, self.head
        
        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev
