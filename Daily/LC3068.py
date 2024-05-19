from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        maxSum = sum(max(n, n^k) for n in nums)
        changedCount = sum((n^k)>n for n in nums)
        if changedCount % 2 == 0:
            return maxSum
        minChangeDiff = min(abs(n-(n^k)) for n in nums)
        return maxSum - minChangeDiff
