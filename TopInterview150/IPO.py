from heapq import heappop, heappush, heapify

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap_by_capital = [(c, p) for c, p in zip(capital, profits)]
        heapify(min_heap_by_capital)
        max_heap_by_profit = []
        # Try do up to k projects
        while k:
            # Move all projects we have capital for to max heap by profit
            while min_heap_by_capital and min_heap_by_capital[0][0] <= w:
                heappush(max_heap_by_profit, -heappop(min_heap_by_capital)[1])
            if not max_heap_by_profit:
                break
            # Do the most profitable project we can afford
            w -= heappop(max_heap_by_profit)
            k -= 1
        return w