from collections import Counter
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithAtMostKDistinct(k: int) -> int:
            ans = 0
            count = Counter()
            left = 0
            for right, num in enumerate(nums):
                count[num] += 1
                if count[num] == 1:
                    k -= 1
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                ans += right - left + 1
            return ans
        return subarraysWithAtMostKDistinct(k) - subarraysWithAtMostKDistinct(k-1)