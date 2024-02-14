from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0): # Handle empty list case.
            return 0
        k: int = 1
        for i in range(1, len(nums)):
            # Find first instances of unique values.
            if nums[i]>nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
