from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        length = len(s)
        dp = [True]+[False]*(length)
        for i in range(1,length+1):
            dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
        return dp[-1]