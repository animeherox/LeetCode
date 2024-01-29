class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        if root is None:
            return 0
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        if left_depth == right_depth:
            # Left tree is full, add the right
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right tree is smaller but complete, so add left
            return (1 << right_depth) + self.countNodes(root.left)
