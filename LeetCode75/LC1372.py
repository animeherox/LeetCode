from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigZag(node: Optional[TreeNode], leftLength: int, rightLength: int):
            if node is None:
                return
            nonlocal maxLength
            maxLength = max(maxLength, leftLength, rightLength)
            zigZag(node.left, rightLength + 1, 0)
            zigZag(node.right, 0, leftLength + 1)
        maxLength = 0
        zigZag(root, 0, 0)
        return maxLength
