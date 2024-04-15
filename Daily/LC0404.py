from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode], isLeft: bool) -> int:
            if node is None:
                return None
            elif node.left and node.right:
                return helper(node.left, True) + helper(node.right, False)
            elif node.left:
                return helper(node.left, True)
            elif node.right:
                return helper(node.right, False)
            return node.val if isLeft else 0
        return helper(root, False)
