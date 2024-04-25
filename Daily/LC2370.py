from string import ascii_lowercase

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        length = len(s)
        dp = [1] * length
        lastIndexDict = {s[0]: 0}
        for i in range(1, length):
            currentAscii = ord(s[i])
            for b in ascii_lowercase:
                if abs(currentAscii - ord(b)) > k:
                    continue
                if b in lastIndexDict:
                    dp[i] = max(dp[i], dp[lastIndexDict[b]]+1)
            lastIndexDict[s[i]] = i
        return max(dp)
