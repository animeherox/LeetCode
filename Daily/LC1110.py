from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleteSet = set(to_delete)
        forest = []
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in deleteSet:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node
        if dfs(root):
            forest.append(root)
        return forest
