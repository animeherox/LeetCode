from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            decrement = max(0, arr[i]-arr[i-1]-1)
            arr[i] -= decrement
        return arr[-1]
