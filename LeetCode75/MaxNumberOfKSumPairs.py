from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        operations = 0
        while left < right:
            pair = nums[left] + nums[right]
            if pair == k:
                left += 1
                right -= 1
                operations += 1
            elif pair < k:
                left += 1
            else:
                right -= 1
        return operations
