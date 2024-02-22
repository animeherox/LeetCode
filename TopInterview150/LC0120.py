from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        numRows = len(triangle)
        dp = [[0]*i for i in range(1, numRows+1)]
        dp[-1] = triangle[-1]
        for i in range(numRows-2, -1, -1):
            # Fill rows from bottom to top
            for j in range(i+1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]