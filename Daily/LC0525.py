from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = maxLength = 0
        balanceMap = {0: -1}
        for i, val in enumerate(nums):
            balance += 1 if val == 1 else -1
            if balance in balanceMap:
                maxLength = max(maxLength, i - balanceMap[balance])
            else:
                balanceMap[balance] = i
        return maxLength
