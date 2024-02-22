class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodeCount = 0
        def dfs(node, maxVal):
            if node is None:
                return
            nonlocal nodeCount
            if maxVal <= node.val:
                nodeCount += 1
                maxVal = node.val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, root.val)
        return nodeCount
