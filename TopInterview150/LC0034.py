from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Reused from problem 35
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftInsert = self.searchInsert(nums, target)
        rightInsert = self.searchInsert(nums, target+1)
        if leftInsert == rightInsert:
            return [-1, -1]
        else:
            return [leftInsert, rightInsert-1]