from heapq import heappush, heappop
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]
