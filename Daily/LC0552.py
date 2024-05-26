class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # Dimensions: Day, # of absences, # of consecutive days late
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n)]
        dp[0][0][0] = 1
        dp[0][1][0] = 1
        dp[0][0][1] = 1
        for i in range(1, n):
            # Late
            dp[i][0][1] = dp[i-1][0][0]
            dp[i][0][2] = dp[i-1][0][1]
            dp[i][1][1] = dp[i-1][1][0]
            dp[i][1][2] = dp[i-1][1][1]
            # Present or Absent
            dp[i][0][0] = sum(dp[i - 1][0][l] for l in range(3)) % MOD
            dp[i][1][0] = sum(dp[i - 1][0][l] + dp[i - 1][1][l] for l in range(3)) % MOD
        total = 0
        for j in range(2):
            for k in range(3):
                total = (total + dp[n-1][j][k]) % MOD
        return total