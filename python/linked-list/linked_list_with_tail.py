class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class TailLinkedList:
    """Python implementation of a singly linked list."""

    def __init__(self, nodes=None):
        """Initialize the linked list."""
        self.head = None
        self.tail = None
        self.count = 0
        if nodes is not None:
            self.count += len(nodes)
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                if node.next is None:
                    self.tail = node

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

    def __len__(self):
        """The length of the linked lint."""
        return self.count

    def add_front(self, node):
        """Add a node to the front of the list. Time complexity: O(1)."""
        node.next = self.head # node é o novo head, portanto o next dele vai apontar para o head atual
        self.head = node # o head agora é o novo node
        self.count += 1
    
    def add_back(self, node):
        """Add a node to the back of the list. Time complexity: O(1)."""
        if self.is_empty():
            self.add_front(node)
            return 
        
        current_tail = self.tail
        current_tail.next = node
        self.tail = node
        self.count += 1

    def add_after(self, target_node, new_node):
        """Add a node after the target node. Time complexity: O(n)."""
        if self.is_empty():
            self.add_front(new_node)
            return
        
        for node in self:
            if node.data == target_node:
                new_node.next = node.next
                node.next = new_node
                
    
    def add_before(self, target_node, new_node):
        """Add a node before the target node. Time complexity: O(n)."""
        if self.is_empty():
            self.add_front(new_node)
            return
        
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
        if self.is_empty():
            raise Exception("Empty list.")
        
        for node in self:
            if node.data == target_node:
                pass
                
    def is_empty(self) -> bool:
        """Returns if linked list is empty."""
        return self.count == 0
    
    def reverse(self):
        """Reverse the lnked list. Time complexity: O(n)."""
        if self.is_empty():
            return
        
        prev_node = self.head
        for node in self:
            node.next = prev_node
            prev_node = node
            
