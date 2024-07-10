from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWait = currentTime = 0
        for arrivalTime, serviceTime in customers:
            currentTime = max(currentTime, arrivalTime)
            currentTime += serviceTime
            totalWait += currentTime - arrivalTime
        return totalWait / len(customers)
