from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numLength = len(nums)
        answer = [1]*numLength

        # First multiply answer[i] by all numbers to left
        leftProduct = 1
        for i in range(numLength):
            answer[i] = leftProduct
            leftProduct *= nums[i]
        
        # Then multiply answer[i] by all numbers to right
        rightProduct = 1
        for i in range(numLength-1, -1, -1):
            answer[i] *= rightProduct
            rightProduct *= nums[i]
        
        return answer