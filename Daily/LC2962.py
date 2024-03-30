from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        n = len(nums)
        ans = 0
        count = 0
        right = 0
        for left, num in enumerate(nums):
            while right < n and count < k:
                count += nums[right] == maxNum
                right += 1
            if count < k:
                break
            ans += n - right + 1
            count -= num == maxNum
        return ans
