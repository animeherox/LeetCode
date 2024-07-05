from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = current
        while current and current.next:
            total = 0
            pointer = current.next
            while pointer.val != 0:
                total += pointer.val
                pointer = pointer.next
            prev = current
            current.val = total
            current.next = pointer
            current = pointer
        prev.next = None
        return head
