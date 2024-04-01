from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        j = prevMinK = prevMaxK = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                j = i
            if num == minK:
                prevMinK = i
            if num == maxK:
                prevMaxK = i
            ans += max(0, min(prevMinK, prevMaxK) - j)
        return ans
