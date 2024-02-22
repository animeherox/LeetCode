from collections import Counter
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathCounts = Counter({0: 1})
        def dfs(node, currentSum):
            if node is None:
                return 0
            currentSum += node.val
            pathCount = pathCounts[currentSum - targetSum]
            pathCounts[currentSum] += 1
            pathCount += dfs(node.left, currentSum)
            pathCount += dfs(node.right, currentSum)
            pathCounts[currentSum] -= 1
            return pathCount
        return dfs(root, 0)
