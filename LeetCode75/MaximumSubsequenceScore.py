from heapq import heappush, heappop
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combinedNums = sorted(zip(nums2, nums1), reverse=True)
        minHeap = []
        currentSum = maxScore = 0
        for num2Val, num1Val in combinedNums:
            currentSum += num1Val
            heappush(minHeap, num1Val)
            if len(minHeap) == k:
                maxScore = max(maxScore, currentSum * num2Val)
                currentSum -= heappop(minHeap)
        return maxScore
