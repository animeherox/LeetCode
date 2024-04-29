from functools import reduce
from operator import xor
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = reduce(xor, nums, k)
        return result.bit_count()
