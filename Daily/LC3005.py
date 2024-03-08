from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxFreq = max(counts.values())
        return sum([v for k, v in counts.items() if v == maxFreq])
