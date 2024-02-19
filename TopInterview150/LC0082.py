from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        # Create dummy head to handle case where current head is removed
        dummyHead = current = ListNode(next=head)
        while current:
            if current.next:
                pointer = current.next
                value = pointer.val
                if pointer.next and pointer.next.val == value:
                    # We've found a duplicate, so remove them all
                    while pointer.next and pointer.next.val == value:
                        pointer = pointer.next
                    current.next = pointer.next
                else:
                    current = current.next
            else:
                current = current.next
        return dummyHead.next