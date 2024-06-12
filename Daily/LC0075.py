from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current, nextZero, nextTwo = 0, -1, len(nums)
        while current < nextTwo:
            if nums[current] == 0:
                nextZero += 1
                nums[nextZero], nums[current] = nums[current], nums[nextZero]
                current += 1
            elif nums[current] == 2:
                nextTwo -= 1
                nums[nextTwo], nums[current] = nums[current], nums[nextTwo]
            else:
                current += 1
