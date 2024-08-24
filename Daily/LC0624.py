from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxDist = 0
        minVal, maxVal = arrays[0][0], arrays[0][-1]
        for array in arrays[1:]:
            maxDist = max(abs(array[-1]-minVal), abs(maxVal-array[0]), maxDist)
            minVal = min(array[0], minVal)
            maxVal = max(array[-1], maxVal)
        return maxDist
