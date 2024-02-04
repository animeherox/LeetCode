from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        min_right_subtree = root.right
        while min_right_subtree.left:
            min_right_subtree = min_right_subtree.left
        root.val = min_right_subtree.val
        root.right = self.deleteNode(root.right, min_right_subtree.val)
        return root
