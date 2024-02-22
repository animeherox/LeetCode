from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        firstHalfHead = head
        secondHalfStart = slow.next
        slow.next = None # Split the lists
        secondHalfHead = reverse(secondHalfStart)
        maxTwinSum = 0
        while firstHalfHead and secondHalfHead:
            maxTwinSum = max(maxTwinSum, firstHalfHead.val + secondHalfHead.val)
            firstHalfHead = firstHalfHead.next
            secondHalfHead = secondHalfHead.next
        return maxTwinSum
