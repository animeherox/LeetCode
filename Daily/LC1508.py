from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarraySums = []
        for i in range(n):
            currentSum = 0
            for j in range(i, n):
                currentSum += nums[j]
                subarraySums.append(currentSum)
        subarraySums.sort()
        modulo = 10**9 + 7
        return sum(subarraySums[left-1:right]) % modulo
