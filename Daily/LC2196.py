from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = defaultdict(TreeNode)
        childSet = set()
        for parentVal, childVal, isLeft in descriptions:
            if parentVal not in nodeMap:
                nodeMap[parentVal] = TreeNode(parentVal)
            if childVal not in nodeMap:
                nodeMap[childVal] = TreeNode(childVal)
            if isLeft:
                nodeMap[parentVal].left = nodeMap[childVal]
            else:
                nodeMap[parentVal].right = nodeMap[childVal]
            childSet.add(childVal)
        for val, node in nodeMap.items():
            if val not in childSet:
                return node
        return None
