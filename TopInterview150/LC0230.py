from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            if root:
                # Always try go left first
                stack.append(root)
                root = root.left
            else:
                # Then go to root, then try right path
                root = stack.pop()
                k -= 1
                if k == 0:
                    # Return immediately at kth element to save time
                    return root.val
                root = root.right