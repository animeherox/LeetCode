from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def getPath(node, target, path, ans):
            if node is None:
                return
            if node.val == target:
                ans.append(''.join(path))
            path.append('L')
            getPath(node.left, target, path, ans)
            path[-1] = 'R'
            getPath(node.right, target, path, ans)
            path.pop(-1)
        
        tmpPath = []
        startPath = []
        destPath = []
        getPath(root, startValue, tmpPath, startPath)
        getPath(root, destValue, tmpPath, destPath)
        startPath = startPath[0]
        destPath = destPath[0]
        
        i = 0
        while i < min(len(startPath), len(destPath)) and startPath[i] == destPath[i]:
            i += 1
        return 'U'*(len(startPath)-i) + destPath[i:]
