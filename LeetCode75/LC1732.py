from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = current = 0
        for g in gain:
            current += g
            maxAltitude = max(maxAltitude, current)
        return maxAltitude
