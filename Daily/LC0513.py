from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxDepth = -1
        leftVal = 0
        def dfs(node: Optional[TreeNode], depth: int):
            nonlocal maxDepth, leftVal
            if node is None:
                return
            if depth > maxDepth:
                maxDepth = depth
                leftVal = node.val
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return leftVal
