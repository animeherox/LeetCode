from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed, maxSpeed = 1, int(1e9)
        while minSpeed < maxSpeed:
            midSpeed = (minSpeed + maxSpeed) >> 1
            midHours = sum((pile + midSpeed - 1) // midSpeed for pile in piles)
            if midHours <= h:
                maxSpeed = midSpeed
            else:
                minSpeed = midSpeed + 1
        return minSpeed
