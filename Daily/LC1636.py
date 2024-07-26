from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return sorted(nums, key=lambda x: counts[x] - x/100000)
