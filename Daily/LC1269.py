class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        base = 10**9 + 7
        dp = [0] * min(steps//2 + 1, arrLen)
        dp[0] = 1
        for _ in range(steps):
            newDp = [0] * min(steps//2 + 1, arrLen)
            for i, ways in enumerate(dp):
                if ways > 0:
                    for dx in (-1, 0, 1):
                        nextI = i+dx
                        if 0 <= nextI < len(dp):
                            newDp[nextI] = (newDp[nextI] + ways) % base
            dp = newDp
        return dp[0]
