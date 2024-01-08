class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: # Handle empty case
            return None
        
        current = head
        # Weave clones into the list
        while current:
            clone = Node(current.val, current.next)
            current.next = clone
            current = clone.next
        
        # Copy random pointers from originals to clone
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next # Connect clones of random pair
            current = current.next.next # Move twice to skip clones
        
        # Disconnect clones from originals
        originalCurrent = head
        cloneHead = head.next
        while originalCurrent:
            cloneCurrent = originalCurrent.next
            originalCurrent.next = cloneCurrent.next
            if cloneCurrent.next:
                cloneCurrent.next = cloneCurrent.next.next
            originalCurrent = originalCurrent.next
        
        return cloneHead