from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            nums[abs(n)-1] *= -1
            if nums[abs(n) - 1] > 0:
                ans.append(abs(n))
        return ans
