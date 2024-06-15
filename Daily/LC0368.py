from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        maxIndex = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[maxIndex] < dp[i]:
                maxIndex = i
        subsetSize = dp[maxIndex]
        currentIndex = maxIndex
        largestSubset = []
        while subsetSize:
            if nums[maxIndex] % nums[currentIndex] == 0 and dp[currentIndex] == subsetSize:
                largestSubset.append(nums[currentIndex])
                maxIndex, subsetSize = currentIndex, subsetSize-1
            currentIndex -= 1
        return largestSubset
