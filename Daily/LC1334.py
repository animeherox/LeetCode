from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dijkstra(u: int) -> int:
            distances = [float('inf')] * n
            distances[u] = 0
            visited = [False] * n
            for _ in range(n):
                k = -1
                for j in range(n):
                    if not visited[j] and (k == -1 or distances[k] > distances[j]):
                        k = j
                visited[k] = True
                for j in range(n):
                    distances[j] = min(distances[j], distances[k] + graph[k][j])
            return sum(d <= distanceThreshold for d in distances)
        graph = [[float('inf')] * n for _ in range(n)]
        for start, end, weight in edges:
            graph[start][end] = graph[end][start] = weight
        ansCity = n
        minReachableCities = float('inf')
        for i in range(n-1, -1, -1):
            reachableCities = dijkstra(i)
            if reachableCities < minReachableCities:
                minReachableCities = reachableCities
                ansCity = i
        return ansCity
