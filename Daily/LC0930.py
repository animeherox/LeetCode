from collections import Counter
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = prefix = 0
        count = Counter({0: 1})
        for n in nums:
            prefix += n
            ans += count[prefix-goal]
            count[prefix] += 1
        return ans
