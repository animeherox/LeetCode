# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        aPtr = list1
        for _ in range(a-1):
            aPtr = aPtr.next
        bPtr = aPtr
        for _ in range(b-a+1):
            bPtr = bPtr.next
        aPtr.next = list2
        current = aPtr.next
        while current.next:
            current = current.next
        current.next = bPtr.next
        return list1
