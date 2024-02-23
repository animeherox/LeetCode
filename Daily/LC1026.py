from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], highest: int, lowest: int):
            if node is None:
                return -INF
            return max(
                dfs(node.left, max(node.val, highest), min(node.val, lowest)),
                dfs(node.right, max(node.val, highest), min(node.val, lowest)),
                highest-node.val,
                node.val-lowest)
        INF = float('inf')
        return dfs(root, -INF, INF)
