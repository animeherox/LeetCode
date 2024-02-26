class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1]+[0]*n # Number of mappings ending at a given value
        dp[0] = 1 if s[0] != '0' else 0
        for i in range(n):
            if i > 0 and 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
            if 1 <= int(s[i]) <= 9:
                dp[i+1] += dp[i]
        return dp[n]
