from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        for current, value in enumerate(nums):
            if value != 0:
                nums[nonZeroIndex], nums[current] = nums[current], nums[nonZeroIndex]
                nonZeroIndex += 1
