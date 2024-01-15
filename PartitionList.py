class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ltHead = ListNode() # Initialize list for values less than x
        geHead = ListNode() # Initialize list for values >= x

        # Initialize pointers moving through/building the lists
        current = head
        currentLt = ltHead
        currentGe = geHead
        while current:
            if current.val < x:
                currentLt.next = current
                currentLt = currentLt.next
            else:
                currentGe.next = current
                currentGe = currentGe.next
            current = current.next
        # Connect the partitioned lists
        currentLt.next = geHead.next
        currentGe.next = None
        return ltHead.next