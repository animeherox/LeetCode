from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Each variable represents the profit after that action executes
        # Ex: First_buy is the "profit" immediately after the first purchase
        # Second_sell is our target, the maximum value after two transactions
        first_buy, first_sell = -prices[0], 0
        second_buy, second_sell = -prices[0], 0

        for price in prices[1:]:
            # Consider updating first buy to the new price
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy+price)
            second_buy = max(second_buy, first_sell-price)
            second_sell = max(second_sell, second_buy+price)
        
        return second_sell
