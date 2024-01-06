class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        # Have one pointer go at twice the speed of the other
        slow = head
        fast = head.next
        while slow != fast: # If slow catches up to fast, a loop must have happened
            if fast == None or fast.next == None:
                return False # If the end is reachable, there is no loop
            slow = slow.next
            fast = fast.next.next
        return True