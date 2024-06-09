from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixCounts = [1] + [0] * (k-1)
        totalSubarrays = 0
        currentSum = 0
        for n in nums:
            currentSum = (currentSum + n) % k
            totalSubarrays += prefixCounts[currentSum]
            prefixCounts[currentSum] += 1
        return totalSubarrays
