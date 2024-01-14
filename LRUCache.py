class Node:
    def __init__(self, key=0, value=0):
        # Initiate a node in the doubly linked list
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize general attributes
        self.cache = {}
        self.capacity = capacity
        self.size = 0

        # Initialize and link head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update node and move to head
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            # Create new node at head
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            # If too large, remove the tail
            if self.size > self.capacity:
                removed_node = self.remove_tail()
                del self.cache[removed_node.key]
                self.size -= 1
        
    def move_to_head(self, node: Node):
        self.remove_node(node)
        self.add_to_head(node)
    
    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node