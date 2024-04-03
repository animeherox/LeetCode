from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        totalSum, length = sum(nums), len(nums)
        ans = [0]*length
        prefixSum = 0
        for i, val in enumerate(nums):
            currentVal = val*i - prefixSum + totalSum - prefixSum - val*(length-i)
            ans[i] = currentVal
            prefixSum += val
        return ans
