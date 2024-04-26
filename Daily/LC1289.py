from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        smallestFall = secondSmallestFall = 0
        smallestFallPos = -1
        for row in grid:
            print(smallestFall, secondSmallestFall)
            currentSmallest = currentSecondSmallest = float('inf')
            currentSmallestPos = -1
            for i, val in enumerate(row):
                totalSum = (secondSmallestFall if i == smallestFallPos else smallestFall) + val
                if totalSum < currentSmallest:
                    currentSecondSmallest = currentSmallest
                    currentSmallest = totalSum
                    currentSmallestPos = i
                elif totalSum < currentSecondSmallest:
                    currentSecondSmallest = totalSum
            smallestFall, secondSmallestFall, smallestFallPos = currentSmallest, currentSecondSmallest, currentSmallestPos
        return smallestFall
