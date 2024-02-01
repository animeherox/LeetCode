class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        max_sum = nums[0]
        dp = [nums[0]]*length
        for i in range(1, length):
            dp[i] = max(0, dp[i-1]) + nums[i]
            max_sum = max(max_sum, dp[i])
        return max_sum