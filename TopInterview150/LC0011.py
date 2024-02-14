from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPtr, rightPtr, maxArea = 0, len(height)-1, 0
        while leftPtr < rightPtr:
            minHeight = min(height[leftPtr], height[rightPtr])
            maxArea = max(maxArea, (rightPtr-leftPtr)*minHeight)
            if height[leftPtr] < height[rightPtr]:
                leftPtr += 1
            else:
                rightPtr -= 1
        return maxArea