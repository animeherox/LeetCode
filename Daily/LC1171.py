from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix = {}
        currentSum, currentNode = 0, dummy
        while currentNode:
            currentSum += currentNode.val
            prefix[currentSum] = currentNode
            currentNode = currentNode.next
        currentSum, currentNode = 0, dummy
        while currentNode:
            currentSum += currentNode.val
            currentNode.next = prefix[currentSum].next
            currentNode = currentNode.next
        return dummy.next
