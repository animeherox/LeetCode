from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustGiven = [0]*n
        trustReceived = [0]*n
        for giver, receiver in trust:
            trustGiven[giver-1] += 1
            trustReceived[receiver-1] += 1
        for i in range(n):
            if trustGiven[i] == 0 and trustReceived[i] == n-1:
                return i+1
        return -1
