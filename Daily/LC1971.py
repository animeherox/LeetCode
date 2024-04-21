from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        def findRoot(node: int) -> int:
            if parent[node] != node:
                parent[node] = findRoot(parent[node])
            return parent[node]
        for start, end in edges:
            parent[findRoot(start)] = findRoot(end)
        return findRoot(source) == findRoot(destination)
