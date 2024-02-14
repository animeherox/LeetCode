from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int = 0 # Also tracks position of last non-val copied.
        for index_read in range(len(nums)):
            if (nums[index_read] != val):
                nums[k] = nums[index_read]
                k += 1
        return k