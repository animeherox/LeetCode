from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = i = 0
        n = len(colors)
        while i < n-1:
            if colors[i] != colors[i+1]:
                # If balloons alternate, we are fine.
                i += 1
            else:
                # If consecutive balloons share color, remove all but one.
                j = i+1
                while j < n-1 and colors[j+1] == colors[i]:
                    j += 1
                totalTime += sum(neededTime[i:j+1]) - max(neededTime[i:j+1])
                i = j+1
        return totalTime
