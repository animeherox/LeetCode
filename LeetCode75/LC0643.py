from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k
        currentSum = maxSum = sum(nums[:k])
        while right < len(nums):
            currentSum += nums[right] - nums[left]
            maxSum = max(maxSum, currentSum)
            left += 1
            right += 1
        return maxSum/k
