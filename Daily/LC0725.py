from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        size, remainder = divmod(length, k)
        current = head
        result = [None for _ in range(k)]
        for i in range(k):
            partHead = current
            partSize = size + (i < remainder)
            for j in range(partSize-1):
                if current:
                    current = current.next
            if current:
                nextPart = current.next
                current.next = None
                current = nextPart
            result[i] = partHead
        return result
