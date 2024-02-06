from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = numFlips = maxConsecutive = 0
        while right < len(nums):
            if nums[right] == 0:
                numFlips += 1
                while numFlips > k:
                    if nums[left] == 0:
                        numFlips -= 1
                    left += 1
            right += 1
            maxConsecutive = max(maxConsecutive, right-left)
        return maxConsecutive
