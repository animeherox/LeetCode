from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallestString = '{'
        def dfs(node, path):
            nonlocal smallestString
            if node:
                path.append(chr(ord('a')+node.val))
                if node.left is None and node.right is None:
                    currentString = ''.join(reversed(path))
                    smallestString = min(smallestString, currentString)
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop()
        dfs(root, [])
        return smallestString
