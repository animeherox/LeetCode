from math import inf, sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        maxRoot = int(sqrt(n))
        dp = [0] + [inf]*n
        for i in range(1, maxRoot+1):
            square = i*i
            for j in range(square, n+1):
                dp[j] = min(dp[j], dp[j - square] + 1)
        return dp[-1]
