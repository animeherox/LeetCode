class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float('inf')
        self.prevVal = -float('inf')

        # Walk through BST in order, comparing values
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            self.minDiff = min(self.minDiff, node.val - self.prevVal)
            self.prevVal = node.val
            traverse(node.right)
        
        traverse(root)

        return self.minDiff