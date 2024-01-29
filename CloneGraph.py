from typing import Optional
class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        visited = defaultdict(Node)
        def clone(node: Optional['Node']) -> Optional['Node']:
            if node is None:
                return None
            if node in visited:
                return visited[node]
            clone_node = Node(node.val)
            visited[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            return clone_node
        return clone(root)
