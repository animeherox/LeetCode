from collections import defaultdict
from math import inf

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ringLength, keyLength = len(ring), len(key)
        charPos = defaultdict(list)
        for i, char in enumerate(ring):
            charPos[char].append(i)
        dp = [[inf]*ringLength for _ in range(keyLength)]
        for j in charPos[key[0]]:
            dp[0][j] = min(j, ringLength-j) + 1
        for i in range(1, keyLength):
            for j in charPos[key[i]]:
                for k in charPos[key[i-1]]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(abs(j - k), ringLength - abs(j - k)) + 1)
        return min(dp[-1][j] for j in charPos[key[-1]])