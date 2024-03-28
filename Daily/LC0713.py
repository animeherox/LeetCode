from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        product = 1
        start = 0
        for end, val in enumerate(nums):
            product *= val
            while start <= end and product >= k:
                product //= nums[start]
                start += 1
            count += end - start + 1
        return count
