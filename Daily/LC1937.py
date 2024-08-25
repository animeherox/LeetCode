from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points[0])
        dp = points[0]
        for row in points[1:]:
            newDp = [0] * n
            leftMax = float('-inf')
            for j in range(n):
                leftMax = max(leftMax, dp[j] + j)
                newDp[j] = max(newDp[j], row[j] + leftMax - j)
            rightMax = float('-inf')
            for j in range(n-1, -1, -1):
                rightMax = max(rightMax, dp[j]-j)
                newDp[j] = max(newDp[j], row[j] + rightMax + j)
            dp = newDp
        return max(dp)
