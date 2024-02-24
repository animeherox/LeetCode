from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        arithmeticCount = [defaultdict(int) for _ in nums]
        totalCount = 0
        for i, current in enumerate(nums):
            for j, prev in enumerate(nums[:i]):
                diff = current - prev
                totalCount += arithmeticCount[j][diff]
                arithmeticCount[i][diff] += arithmeticCount[j][diff] + 1
        return totalCount
