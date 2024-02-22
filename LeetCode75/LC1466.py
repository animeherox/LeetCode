from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node):
            visited[node] = True
            count = 0
            for connectedNode in adjacencyList[node]:
                if not visited[connectedNode]:
                    if (node, connectedNode) in directedEdges:
                        count += 1
                    count += dfs(connectedNode)
            return count
        
        adjacencyList = defaultdict(list)
        directedEdges = set()
        for a, b in connections:
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)
            directedEdges.add((a,b))
        visited = [False]*n
        return dfs(0)
