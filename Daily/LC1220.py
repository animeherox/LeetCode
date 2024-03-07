class Solution:
    def countVowelPermutation(self, n: int) -> int:
        base = 10**9 + 7
        dp = [1] * 5
        for _ in range(1, n):
            dp = [
                (dp[1] + dp[2] + dp[4]) % base,
                (dp[0] + dp[2]) % base,
                (dp[1] + dp[3]) % base,
                (dp[2]) % base,
                (dp[2] + dp[3]) % base
            ]
        return sum(dp) % base
