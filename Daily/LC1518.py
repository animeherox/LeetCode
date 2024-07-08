class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            total += newBottles
            numBottles = numBottles - (newBottles * (numExchange - 1))
        return total
