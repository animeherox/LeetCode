from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        costs = [INF]*n
        costs[src] = 0
        for _ in range(k+1):
            costsBackup = costs.copy()
            for start, end, price in flights:
                costs[end] = min(costs[end], costsBackup[start]+price)
        return costs[dst] if costs[dst] != INF else -1
