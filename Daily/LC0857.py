from heapq import heappush, heappop
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(zip(quality, wage), key = lambda x: x[1]/x[0])
        minCost = float('inf')
        totalQuality = 0
        maxHeap = []
        for q, w in workers:
            totalQuality += q
            heappush(maxHeap, -q)
            if len(maxHeap) > k:
                totalQuality += heappop(maxHeap)
            if len(maxHeap) == k:
                minCost = min(minCost, w/q*totalQuality)
        return minCost
