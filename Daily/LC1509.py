from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0
        else:
            nums.sort()
            return min(nums[n - 4 + l] - nums[l] for l in range(4))
