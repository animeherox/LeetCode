from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base case where list is 0-1 nodes long
        if head is None or head.next is None:
            return head
        # Step 1: Compute length
        current, length = head, 0
        while current:
            length += 1
            current = current.next
        k %= length
        # If the length of the list divides k, no rotation is needed
        if k == 0:
            return head
        fast, slow = head, head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
