from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set(nums)
        dummyHead = ListNode(next=head)
        current = dummyHead
        while current.next:
            if current.next.val in numSet:
                current.next = current.next.next
            else:
                current = current.next
        return dummyHead.next
