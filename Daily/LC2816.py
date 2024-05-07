from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getCarry(node: Optional[ListNode]) -> int:
            val = node.val * 2
            if node.next:
                val += getCarry(node.next)
            node.val = val % 10
            return val // 10
        if getCarry(head):
            return ListNode(1, head)
        return head
