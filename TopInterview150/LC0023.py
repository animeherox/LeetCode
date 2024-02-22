from queue import PriorityQueue
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class ComparableListNode:
    def __init__(self, node: ListNode):
        self.val = node.val
        self.next = node.next
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Add all lists to priority queue
        pq = PriorityQueue()
        for head in lists:
            if head:
                pq.put(ComparableListNode(head))
        
        # Add nodes to answer, one head at a time from heap
        dummyHead = current = ListNode()
        while not pq.empty():
            node = pq.get()
            if node.next:
                pq.put(ComparableListNode(node.next))
            current.next = node
            current = current.next
        
        return dummyHead.next