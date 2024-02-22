from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end)//2
            # Check if midpoint is before a pivot
            if nums[0] <= nums[mid]:
                # If target is in range, go left
                if nums[0] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            # If midpoint is after pivot, the logic flips
            else:
                if nums[mid] < target <= nums[-1]:
                    start = mid + 1
                else:
                    end = mid
        return start if nums[start]==target else -1