from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow.next
        while current:
            temp = current.next
            current.next = prev
            prev, current = current, temp
        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        return True
