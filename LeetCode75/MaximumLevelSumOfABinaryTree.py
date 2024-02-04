from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        currentLevel = 0
        maxLevel = 0
        maxSum = -float('inf')
        queue = deque([root])
        while queue:
            currentLevel += 1
            levelSum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = currentLevel
        return maxLevel
