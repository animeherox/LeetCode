from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return
            nonlocal ans, counter
            counter[node.val] += 1
            if node.left is None and node.right is None:
                oddCount = [1 for i in range(1, 10) if counter[i] % 2 == 1]
                if sum(oddCount) < 2:
                    ans += 1
            else:
                dfs(node.left)
                dfs(node.right)
            counter[node.val] -= 1
        counter = [0] * 10
        ans = 0
        dfs(root)
        return ans
