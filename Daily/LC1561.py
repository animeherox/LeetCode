from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        numPiles = len(piles)
        n = numPiles // 3
        return sum([piles[-2-2*i] for i in range(n)])
