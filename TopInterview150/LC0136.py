from functools import reduce
from operator import xor
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # For all doubled numbers, applying XOR twice cancels out
        return reduce(xor, nums)