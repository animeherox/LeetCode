from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        if root is None:
            return averages
        queue = deque([root])
        while queue:
            total = 0
            count = len(queue)
            # Sum current level while filling queue with the next level
            for _ in range(count):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            averages.append(total/count)
        return averages