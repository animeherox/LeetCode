from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameterHelper(node: Optional[TreeNode]) -> tuple[int, int]: # Diameter, height
            if node is None:
                return 0, -1
            leftResult = diameterHelper(node.left)
            rightResult = diameterHelper(node.right)
            diameter = max(leftResult[0], rightResult[0], leftResult[1]+rightResult[1]+2)
            height = max(leftResult[1], rightResult[1]) + 1
            return diameter, height
        return diameterHelper(root)[0]
