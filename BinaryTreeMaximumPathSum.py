class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best_path = -float('inf')
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal best_path
            if not node:
                return 0
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            best_path = max(best_path, node.val + left_sum + right_sum)
            return node.val + max(left_sum, right_sum)
        dfs(root)
        return best_path
