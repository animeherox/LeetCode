from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = [(arr[0]/arr[j], 0, j) for j in range(1, len(arr))]
        heapify(minHeap)
        for _ in range(k-1):
            smallestFraction, i, j = heappop(minHeap)
            if i+1 < j:
                newFraction = (arr[i+1] / arr[j], i+1, j)
                heappush(minHeap, newFraction)
        _, numIndex, denomIndex = minHeap[0]
        return [arr[numIndex], arr[denomIndex]]
