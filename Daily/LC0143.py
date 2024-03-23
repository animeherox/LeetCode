from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalf = slow.next
        slow.next = None
        prev = None
        current = secondHalf
        while current:
            temp = current.next
            current.next = prev
            prev, current = current, temp
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf, secondHalf = temp1, temp2
