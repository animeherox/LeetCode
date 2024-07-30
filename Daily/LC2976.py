from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[float('inf')]*26 for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0
        for originalChar, changedChar, weight in zip(original, changed, cost):
            x, y = ord(originalChar) - ord('a'), ord(changedChar) - ord('a')
            graph[x][y] = min(graph[x][y], weight)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        totalCost = 0
        for sourceChar, targetChar in zip(source, target):
            if sourceChar != targetChar:
                x, y = ord(sourceChar) - ord('a'), ord(targetChar) - ord('a')
                if graph[x][y] >= float('inf'):
                    return -1
                totalCost += graph[x][y]
        return totalCost
