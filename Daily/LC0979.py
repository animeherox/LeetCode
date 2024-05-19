from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            leftBalance = dfs(node.left)
            rightBalance = dfs(node.right)
            nonlocal movesCount
            movesCount += abs(leftBalance) + abs(rightBalance)
            return leftBalance + rightBalance + node.val - 1
        movesCount = 0
        dfs(root)
        return movesCount
