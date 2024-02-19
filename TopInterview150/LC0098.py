from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Return whether the tree is a valid DFS, whether the left value is
        def dfs(node):
            if not node:
                return True, float('inf'), -float('inf')
            left_result, left_min, left_max = dfs(node.left)
            if not left_result or left_max>=node.val:
                return False, float('inf'), -float('inf')
            right_result, right_min, right_max = dfs(node.right)
            if not right_result or right_min<=node.val:
                return False, float('inf'), -float('inf')
            else:
                return True, min(left_min, node.val), max(right_max, node.val)
        return dfs(root)[0]
