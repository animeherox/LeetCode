from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit: int = 0
        for i in range(1, len(prices)):
            if (prices[i]>prices[i-1]): # Buy rises, ignore drops
                totalProfit += prices[i]-prices[i-1]
        return totalProfit