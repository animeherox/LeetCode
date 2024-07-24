from collections import defaultdict, deque
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def findTopologicalOrder(conditions: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            indegree = [0] * (k+1)
            for u,v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            queue = deque([node for node in range(1, k+1) if indegree[node] == 0])
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            return order if len(order) == k else None
        rowOrder = findTopologicalOrder(rowConditions)
        colOrder = findTopologicalOrder(colConditions)
        if rowOrder is None or colOrder is None:
            return []
        matrix = [[0]*k for _ in range(k)]
        colPosition = [0] * (k+1)
        for position, element in enumerate(colOrder):
            colPosition[element] = position
        for position, element in enumerate(rowOrder):
            col = colPosition[element]
            matrix[position][col] = element
        return matrix
