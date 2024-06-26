# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        totalSum = 0
        current = root
        while current:
            if current.right is None:
                totalSum += current.val
                current.val = totalSum
                current = current.left
            else:
                predecessor = current.right
                while predecessor.left and predecessor.left != current:
                    predecessor = predecessor.left
                if predecessor.left is None:
                    predecessor.left = current
                    current = current.right
                else:
                    totalSum += current.val
                    current.val = totalSum
                    predecessor.left = None
                    current = current.left
        return root
