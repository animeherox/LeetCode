from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left) if left else 0, max([n-ant for ant in right]) if right else 0)
