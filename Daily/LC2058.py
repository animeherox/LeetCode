from math import inf
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, current = head, head.next
        firstCritical = lastCritical = None
        i = 1
        minDist, maxDist = inf, -inf
        while current.next:
            if current.val < min(current.next.val, prev.val) or \
                current.val > max(current.next.val, prev.val):
                if lastCritical is None:
                    firstCritical = lastCritical = i
                else:
                    minDist = min(minDist, i - lastCritical)
                    maxDist = i - firstCritical
                    lastCritical = i
            i += 1
            prev, current = current, current.next
        return [minDist, maxDist] if firstCritical != lastCritical else [-1, -1]
