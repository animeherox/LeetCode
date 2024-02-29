from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal1 = maxVal2 = 0
        for n in nums:
            if n > maxVal1:
                maxVal2 = maxVal1
                maxVal1 = n
            elif n > maxVal2:
                maxVal2 = n
        return (maxVal1 - 1) * (maxVal2 - 1)
