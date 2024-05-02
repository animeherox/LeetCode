from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        while nums[left] < 0 and nums[right] > 0:
            if -nums[left] == nums[right]:
                return nums[right]
            elif -nums[left] > nums[right]:
                left += 1
            else:
                right -= 1
        return -1
