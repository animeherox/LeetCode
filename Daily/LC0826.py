from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        jobs = sorted(zip(difficulty, profit))
        print(jobs)
        worker.sort()
        maxProfit = 0
        totalProfit = 0
        jobIndex = 0
        for w in worker:
            while jobIndex < n and jobs[jobIndex][0] <= w:
                maxProfit = max(maxProfit, jobs[jobIndex][1])
                jobIndex += 1
            totalProfit += maxProfit
        return totalProfit
