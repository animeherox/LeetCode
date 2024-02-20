from collections import defaultdict
from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def countSubarraysWithTargetSum(nums: List[int]) -> int:
            prefixSumCounts = defaultdict(int)
            prefixSumCounts[0] = 1
            count = prefixSum = 0
            for num in nums:
                prefixSum += num
                count += prefixSumCounts[prefixSum-target]
                prefixSumCounts[prefixSum] += 1
            return count
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for startRow in range(m):
            columnSums = [0] * n
            for endRow in range(startRow, m):
                for col in range(n):
                    columnSums[col] += matrix[endRow][col]
                ans += countSubarraysWithTargetSum(columnSums)
        return ans
