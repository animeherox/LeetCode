from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if root is None:
            return view
        queue = deque([root])
        while queue:
            view.append(queue[-1].val) # Add last value on layer
            # Add next layer to queue in order
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return view