class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        
        # Handle edge case involving reverting head
        dummyHead = ListNode(0, head)
        preReverse = dummyHead

        # Move to left of reverse sequence
        for _ in range(left-1):
            preReverse = preReverse.next
        
        # Reverse subsequence
        reverseStart = preReverse.next
        current = reverseStart
        predecessor = preReverse
        for _ in range(right-left+1):
            tempNext = current.next
            current.next = predecessor
            predecessor, current = current, tempNext
        
        # Reconnect the rest of the list
        preReverse.next = predecessor
        reverseStart.next = current

        return dummyHead.next