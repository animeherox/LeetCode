from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        queue = deque()
        for i, val in enumerate(nums):
            if queue and i-queue[0] > k:
                queue.popleft()
            dp[i] = max(0, dp[queue[0]] if queue else 0) + val
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
            queue.append(i)
        return max(dp)
