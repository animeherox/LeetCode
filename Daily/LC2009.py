from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        minOps = n
        windowStart = 0
        for windowEnd, val in enumerate(nums):
            while windowStart < len(nums) and nums[windowStart] - val <= n-1:
                windowStart += 1
            minOps = min(minOps, n - (windowStart - windowEnd))
        return minOps
