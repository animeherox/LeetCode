from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            maxElement = 0
            for j in range(i, max(0, i-k), -1):
                maxElement = max(maxElement, arr[j-1])
                dp[i] = max(dp[i], dp[j-1] + maxElement * (i - j + 1))
        return dp[-1]
