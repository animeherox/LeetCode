from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ansGrid = [[0]*(n-2) for _ in range(n-2)]
        for row in range(n-2):
            for col in range(n-2):
                ansGrid[row][col] = max(
                    grid[i][j] for i in range(row, row+3) for j in range(col, col+3)
                )
        return ansGrid
