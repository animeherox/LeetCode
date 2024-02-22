from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next = slow.next.next
        return dummy.next
