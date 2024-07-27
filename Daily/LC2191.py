from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedWithIndex = []
        for i, num in enumerate(nums):
            mappedNum = mapping[0] if num == 0 else 0
            powerOfTen = 1
            while num:
                num, digit = divmod(num, 10)
                mappedNum = mapping[digit] * powerOfTen + mappedNum
                powerOfTen *= 10
            mappedWithIndex.append((mappedNum, i))
        mappedWithIndex.sort()
        return [nums[i] for _, i in mappedWithIndex]
