# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)
            subtreeSum = leftSum + rightSum + node.val
            subtreeCount = leftCount + rightCount + 1
            if subtreeSum // subtreeCount == node.val:
                nonlocal ans
                ans += 1
            return subtreeSum, subtreeCount
        ans = 0
        dfs(root)
        return ans
