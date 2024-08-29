from functools import lru_cache
from itertools import accumulate
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(currentIndex, maxTake):
            if maxTake * 2 >= totalPiles - currentIndex:
                return prefixSum[totalPiles] - prefixSum[currentIndex]
            return max(
                prefixSum[totalPiles] - prefixSum[currentIndex] - 
                dfs(
                    currentIndex + x,
                    max(maxTake, x)
                ) for x in range(1, 2*maxTake+1)
            )
        totalPiles = len(piles)
        prefixSum = list(accumulate(piles, initial=0))
        return dfs(0, 1)
