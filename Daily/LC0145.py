from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        while root:
            if root.right is None:
                result.append(root.val)
                root = root.left
            else:
                predecessor = root.right
                while predecessor.left and predecessor.left != root:
                    predecessor = predecessor.left
                if predecessor.left != root:
                    result.append(root.val)
                    predecessor.left = root
                    root = root.right
                else:
                    predecessor.left = None
                    root = root.left
        return result[::-1]
