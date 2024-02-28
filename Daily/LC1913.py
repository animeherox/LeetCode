from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        minVal1 = minVal2 = float('inf')
        maxVal1 = maxVal2 = 0
        for i, val in enumerate(nums):
            if val < minVal1:
                minVal2 = minVal1
                minVal1 = val
            elif val < minVal2:
                minVal2 = val
            if val > maxVal1:
                maxVal2 = maxVal1
                maxVal1 = val
            elif val > maxVal2:
                maxVal2 = val
        return maxVal1 * maxVal2 - minVal1 * minVal2
