from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[float('inf')]*amount
        for coin in coins:
            for current_amount in range(coin, amount+1):
                dp[current_amount] = min(dp[current_amount], dp[current_amount-coin]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]
