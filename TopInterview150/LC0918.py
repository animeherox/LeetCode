from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Track both max and min. The max covers the case where we don't loop,
        # while the min covers the case where the max subarray loops around.
        max_sum_end_here = min_sum_end_here = max_subarray_sum = min_subarray_sum = nums[0]
        for n in nums[1:]:
            # Find partial sums ending at n, either restarting or continuing
            max_sum_end_here = n + max(max_sum_end_here, 0)
            min_sum_end_here = n + min(min_sum_end_here, 0)
            # Update overall max/min if appropriate
            max_subarray_sum = max(max_subarray_sum, max_sum_end_here)
            min_subarray_sum = min(min_subarray_sum, min_sum_end_here)
        if max_subarray_sum <= 0:
            return max_subarray_sum
        else:
            return max(max_subarray_sum, sum(nums)-min_subarray_sum)
