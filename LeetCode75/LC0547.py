from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(currentCity: int):
            visited[currentCity] = True
            for neighbor, connected in enumerate(isConnected[currentCity]):
                if connected and not visited[neighbor]:
                    dfs(neighbor)
        n = len(isConnected)
        visited = [False]*n
        count = 0
        for city in range(n):
            if not visited[city]:
                count += 1
                dfs(city)
        return count
