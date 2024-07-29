from random import randint
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(left, right):
            if left >= right:
                return
            pivot = nums[randint(left, right)]
            ltPtr, gtPtr, current = left-1, right+1, left
            while current < gtPtr:
                if nums[current] < pivot:
                    ltPtr += 1
                    nums[ltPtr], nums[current] = nums[current], nums[ltPtr]
                    current += 1
                elif nums[current] > pivot:
                    gtPtr -= 1
                    nums[gtPtr], nums[current] = nums[current], nums[gtPtr]
                else:
                    current += 1
            quickSort(left, ltPtr)
            quickSort(gtPtr, right)
        quickSort(0, len(nums)-1)
        return nums
