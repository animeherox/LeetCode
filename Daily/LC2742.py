from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        kMax = 5*10**8
        dp = [0] + [kMax]*n
        for c, t in zip(cost, time):
            for walls in range(n, 0, -1):
                dp[walls] = min(dp[walls], dp[max(walls-t-1, 0)]+c)
        return dp[n]
