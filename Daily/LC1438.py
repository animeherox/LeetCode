from heapq import heappush, heappop
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeap = [(float('inf'), len(nums))]
        minHeap = [(float('inf'), len(nums))]
        maxLeft = minLeft = -1
        ans = 0
        for i, num in enumerate(nums):
            while -maxHeap[0][0] > num + limit or maxHeap[0][1] < maxLeft:
                maxLeft = max(maxLeft, heappop(maxHeap)[1])
            heappush(maxHeap, (-num, i))
            while minHeap[0][0] < num - limit or minHeap[0][1] < minLeft:
                minLeft = max(minLeft, heappop(minHeap)[1])
            heappush(minHeap, (num, i))
            ans = max(ans, i - max(maxLeft, minLeft))
        return ans
