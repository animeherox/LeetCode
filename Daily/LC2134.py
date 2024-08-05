from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        oneCount, length = nums.count(1), len(nums)
        prefixSum = [0] * ((length << 1) + 1)
        for i in range(length << 1):
            prefixSum[i+1] = prefixSum[i] + nums[i % length]
        maxOnesFound = 0
        for i in range(length << 1):
            endIndex = i + oneCount - 1
            if endIndex < (length << 1):
                maxOnesFound = max(maxOnesFound, prefixSum[endIndex + 1] - prefixSum[i])
        return oneCount - maxOnesFound
