from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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