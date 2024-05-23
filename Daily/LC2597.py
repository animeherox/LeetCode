from collections import Counter
from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i: int):
            nonlocal beautifulCount
            if i >= len(nums):
                beautifulCount += 1
                return
            dfs(i+1)
            if count[nums[i] + k] == 0 and count[nums[i] - k] == 0:
                count[nums[i]] += 1
                dfs(i+1)
                count[nums[i]] -= 1
        beautifulCount = -1 # -1 to balance the empty set
        count = Counter()
        dfs(0)
        return beautifulCount
