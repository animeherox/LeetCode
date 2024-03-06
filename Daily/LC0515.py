from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            rowMax = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                rowMax = max(rowMax, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(rowMax)
        return result
