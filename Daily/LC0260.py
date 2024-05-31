from functools import reduce
from operator import xor
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorAll = reduce(xor, nums)
        rightmostSetBit = xorAll & -xorAll
        uniqueNum1 = 0
        for num in nums:
            if num & rightmostSetBit:
                uniqueNum1 ^= num
        uniqueNum2 = xorAll ^ uniqueNum1
        return [uniqueNum1, uniqueNum2]
