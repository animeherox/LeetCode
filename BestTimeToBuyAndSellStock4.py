class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Table stores maximum values for i transactions, where top row is
        # holding the stock, and bottom row is not. Initialize with buying
        # on the first day.
        profits = [[0, -prices[0]] for _ in range(k + 1)]
        profits[0][1] = 0
        for price in prices[1:]:
            for j in range(k, 0, -1):
                profits[j][0] = max(profits[j][1] + price, profits[j][0])
                profits[j][1] = max(profits[j-1][0] - price, profits[j][1])
        return profits[k][0]