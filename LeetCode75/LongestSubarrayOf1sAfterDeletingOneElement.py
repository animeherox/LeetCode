class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left_ones_count = [0]*n
        right_ones_count = [0]*n
        for i in range(1, n):
            if nums[i-1] == 1:
                left_ones_count[i] = left_ones_count[i-1]+1
        for i in range(n-2, -1, -1):
            if nums[i+1] == 1:
                right_ones_count[i] = right_ones_count[i+1]+1
        return max(a + b for a, b in zip(left_ones_count, right_ones_count))
