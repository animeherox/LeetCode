class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            dummy = Node()
            connector = dummy
            while node:
                if node.left:
                    connector.next = node.left
                    connector = connector.next
                if node.right:
                    connector.next = node.right
                    connector = connector.next
                node = node.next
            node = dummy.next
        return root