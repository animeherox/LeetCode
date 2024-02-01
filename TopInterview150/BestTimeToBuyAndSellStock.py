class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggestProfit: int = 0
        buyPrice: int = prices[0]
        for price in prices:
            print(buyPrice)
            if price <= buyPrice: # If we find a new cheapest price, use it
                buyPrice = price
            elif (price-buyPrice) > biggestProfit:
                biggestProfit = price - buyPrice
        return biggestProfit
