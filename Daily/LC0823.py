from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        base = 10**9 + 7
        n = len(arr)
        arr.sort()
        indexDict = {val: i for i, val in enumerate(arr)}
        dp = [1] * n
        for i, a in enumerate(arr):
            for j in range(i):
                b = arr[j]
                if a % b == 0:
                    c = a // b
                    if c in indexDict:
                        dp[i] = (dp[i] + dp[j] * dp[indexDict[c]]) % base
        return sum(dp) % base
