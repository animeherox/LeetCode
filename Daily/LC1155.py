class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        base = 10**9 + 7
        dp = [1] + [0]*target
        for i in range(1, n+1):
            newDp = [0] * (target + 1)
            for sumVal in range(1, min(i*k, target)+1):
                for faceVal in range(1, min(sumVal, k)+1):
                    newDp[sumVal] = (newDp[sumVal] + dp[sumVal-faceVal]) % base
            dp = newDp
        return dp[target]
