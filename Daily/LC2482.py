from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rowSums = [0]*m
        colSums = [0]*n
        for i in range(m):
            for j in range(n):
                rowSums[i] += grid[i][j]
                colSums[j] += grid[i][j]
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = (2 * rowSums[i] - n) + (2 * colSums[j] - m)
        return diff
