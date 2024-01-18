class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, current_sum: int) -> int:
            if not node:
                return 0
            current_sum = current_sum*10 + node.val
            if not node.left and not node.right:
                return current_sum
            else:
                return dfs(node.left, current_sum)+dfs(node.right, current_sum)
        return dfs(root, 0)
