from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq = []
        n = len(costs)
        left_bound = candidates - 1
        right_bound = n - candidates
        for i in range(candidates):
            pq.append((costs[i], i))
        for i in range(n-candidates, n):
            if i > left_bound:
                pq.append((costs[i], i))
        heapify(pq)
        total_cost = 0
        for _ in range(k):
            cost, index = heappop(pq)
            total_cost += cost
            if index <= left_bound:
                left_bound += 1
                if left_bound < right_bound:
                    heappush(pq, (costs[left_bound], left_bound))
            if index >= right_bound:
                right_bound -= 1
                if right_bound > left_bound:
                    heappush(pq, (costs[right_bound], right_bound))
        return total_cost
