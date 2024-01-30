class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(node: Optional[ListNode]) -> Optional[ListNode]:
            prev, current = None, node
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev
        # Help with cases where the head changes
        dummyHead = ListNode()
        dummyHead.next = head
        prev_group = dummyHead
        while head:
            count = 0
            current = head
            while count < k and current:
                current = current.next
                count += 1
            # If we have at least k nodes left, detach and reverse
            if count == k:
                group_end = head
                for _ in range(k - 1): # Move to the end of the k group
                    group_end = group_end.next
                next_group = group_end.next
                group_end.next = None
                new_head = reverseList(head)
                prev_group.next = new_head
                head.next = next_group
                prev_group = head
                head = next_group
            else:
                # If we have some number of nodes left less than k, we leave them
                break
        return dummyHead.next
