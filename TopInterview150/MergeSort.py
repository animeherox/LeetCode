# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # First, split the lists
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        leftHalf, rightHalf = self.sortList(head), self.sortList(temp)

        # Then merge the two halves
        dummyHead = ListNode()
        current = dummyHead
        while leftHalf and rightHalf:
            if leftHalf.val <= rightHalf.val:
                current.next = ListNode(leftHalf.val)
                leftHalf = leftHalf.next
            else:
                current.next = ListNode(rightHalf.val)
                rightHalf = rightHalf.next
            current = current.next
        # Add leftover portions
        if leftHalf:
            current.next = leftHalf
        else:
            current.next = rightHalf
        return dummyHead.next