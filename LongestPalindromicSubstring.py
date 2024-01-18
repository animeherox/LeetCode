class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        # The first letter will always be a 1-letter palindrome
        start = 0
        max_length = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and dp[i+1][j-1]:
                    if max_length < j-i+1:
                        start = i
                        max_length = j-i+1
                else:
                    dp[i][j] = False
        return s[start:start+max_length]