from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        twoStep, oneStep = cost[0], cost[1]
        for c in cost[2:]:
            twoStep, oneStep = oneStep, min(twoStep, oneStep) + c
        return oneStep
