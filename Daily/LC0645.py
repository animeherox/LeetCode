from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = 0
        for i, value in enumerate(nums, 1):
            result ^= i ^ value
        rightBit = result & -result
        a = 0
        for i, value in enumerate(nums, 1):
            if i & rightBit:
                a ^= i
            if value & rightBit:
                a ^= value
        b = result ^ a
        if a in nums:
            return [a, b]
        else:
            return [b, a]
