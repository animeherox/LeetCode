from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node, leafCountAtDepth, currentDepth):
            if node is None or currentDepth >= distance:
                return
            if node.left is None and node.right is None:
                leafCountAtDepth[currentDepth] += 1
                return
            dfs(node.left, leafCountAtDepth, currentDepth+1)
            dfs(node.right, leafCountAtDepth, currentDepth+1)
        if root is None:
            return 0
        totalPairs = self.countPairs(root.left, distance) + self.countPairs(root.right, distance)
        leftLeafCounter = Counter()
        rightLeafCounter = Counter()
        dfs(root.left, leftLeafCounter, 1)
        dfs(root.right, rightLeafCounter, 1)
        for depthLeft, countLeft in leftLeafCounter.items():
            for depthRight, countRight in rightLeafCounter.items():
                if depthLeft + depthRight <= distance:
                    totalPairs += countLeft * countRight
        return totalPairs
