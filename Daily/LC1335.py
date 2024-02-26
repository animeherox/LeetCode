from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # Options: Do a job on a day, or wait for the next day
        n = len(jobDifficulty)
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, min(d+1, i+1)):
                lastDayDiff = 0
                for k in range(i, 0, -1):
                    lastDayDiff = max(lastDayDiff, jobDifficulty[k - 1])
                    dp[i][j] = min(dp[i][j], dp[k-1][j-1]+lastDayDiff)
        return -1 if dp[n][d] == float('inf') else dp[n][d]
