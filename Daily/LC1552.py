from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canPlace(minDist: int) -> bool:
            prevPos = position[0]
            count = 1
            for currentPos in position[1:]:
                if currentPos - prevPos >= minDist:
                    prevPos = currentPos
                    count += 1
            return count >= m
        position.sort()
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1)//2
            if canPlace(mid):
                left = mid
            else:
                right = mid - 1
        return left
