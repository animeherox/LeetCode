from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = deque([root])
        left_to_right = True
        while queue:
            level_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left_to_right:
                result.append(level_values)
            else:
                result.append(level_values[::-1])
            left_to_right = not left_to_right
        return result
