from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right, n = 0, 1, len(nums)
        maxFreq, totalDiff = 1, 0
        while right < n:
            totalDiff += (nums[right] - nums[right-1]) * (right - left)
            while totalDiff > k:
                totalDiff -= nums[right] - nums[left]
                left += 1
            right += 1
            maxFreq = max(maxFreq, right-left)
        return maxFreq
