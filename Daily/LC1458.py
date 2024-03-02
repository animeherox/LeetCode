from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        dp = [[float('-inf')] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dotProduct = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], max(dp[i - 1][j - 1], 0) + dotProduct)
        return dp[-1][-1]
