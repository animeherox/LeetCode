from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [n**2 for n in nums]
        return sorted(squares)
