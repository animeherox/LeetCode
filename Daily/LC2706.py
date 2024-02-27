from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        minSum = prices[0] + prices[1]
        if minSum <= money:
            return money - minSum
        else:
            return money
