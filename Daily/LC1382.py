# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nodeValues.append(node.val)
            inorder(node.right)
        
        def buildBalancedBst(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nodeValues[mid])
            node.left = buildBalancedBst(start, mid-1)
            node.right = buildBalancedBst(mid+1, end)
            return node
        
        nodeValues = []
        inorder(root)
        return buildBalancedBst(0, len(nodeValues)-1)
