from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def bfs(start: int):
            queue = deque([start])
            visited = {start}
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        ancestors[neighbor].append(start)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        ancestors = [[] for _ in range(n)]
        for node in range(n):
            bfs(node)
        return ancestors
