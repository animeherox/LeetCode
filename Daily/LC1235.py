from bisect import bisect_left
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        numJobs = len(startTime)
        dp = [0] * (numJobs + 1)
        for i in range(numJobs):
            startTime[i] = jobs[i][0]
        for i in reversed(range(numJobs)):
            j = bisect_left(startTime, jobs[i][1])
            dp[i] = max(dp[i+1], dp[j]+jobs[i][2])
        return dp[0]
