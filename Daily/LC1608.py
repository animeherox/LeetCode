from itertools import pairwise
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] >= n:
            return n
        for i, (a,b) in enumerate(pairwise(nums)):
            count = n - i - 1
            if a < count and b >= count:
                return count
        return -1
