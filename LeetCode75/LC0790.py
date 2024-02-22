class Solution:
    def numTilings(self, n: int) -> int:
        kMod = 10**9 + 7
        dp = [0, 1, 2, 5] + [0]*max(0, n - 3)
        for i in range(4, n+1):
            dp[i] = 2 * dp[i-1] + dp[i-3]
        return dp[n] % kMod
