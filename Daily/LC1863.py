from functools import reduce
from operator import or_
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(or_, nums) << len(nums) - 1
