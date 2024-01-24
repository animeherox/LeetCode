class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        current_node = self.stack.pop()
        node = current_node.right
        while node:
            self.stack.append(node)
            node = node.left
        return current_node.val        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
