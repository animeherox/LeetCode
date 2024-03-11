from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minutes = sorted([(d-1)//s for d, s in zip(dist, speed)])
        for i, minute in enumerate(minutes):
            if minute < i:
                return i
        return len(minutes)
