from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root is None:
            return result
        stack = [root]
        while stack:
            current = stack.pop()
            result.append(current.val)
            stack += current.children
        return result[::-1]