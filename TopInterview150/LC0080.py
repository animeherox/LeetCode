from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0): # Handle empty list case.
            return 0
        i: int = 0
        for num in nums:
            if i<2 or num != nums[i-2]:
                nums[i] = num
                i += 1
        return i