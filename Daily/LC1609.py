from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        oddLevel = True
        queue = deque([root])
        while queue:
            lastVal = -float('inf') if oddLevel else float('inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if (oddLevel and node.val > lastVal and node.val % 2 == 1) or (not oddLevel and node.val < lastVal and node.val % 2 == 0):
                    lastVal = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    print(node.val)
                    return False
            oddLevel = not oddLevel
        return True
