from bisect import bisect_left
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def countPairsWithinDistance(dist: int) -> int:
            count = 0
            for i, upperBound in enumerate(nums):
                lowerBound = upperBound - dist
                j = bisect_left(nums, lowerBound, 0, i)
                count += i - j
            return count
        nums.sort()
        maxDist = nums[-1] - nums[0]
        smallestDist = bisect_left(range(maxDist + 1), k, key=countPairsWithinDistance)
        return smallestDist
