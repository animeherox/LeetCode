from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        if 1 in counts.values():
            return -1
        return sum(((count + 2) // 3 for count in counts.values()))
