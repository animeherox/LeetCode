class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        current = head
        while current:
            nextNode = current.next
            current.next = dummyHead.next
            dummyHead.next = current
            current = nextNode
        return dummyHead.next
