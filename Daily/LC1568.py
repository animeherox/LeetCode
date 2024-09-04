from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int):
            grid[row][col] = 2
            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            for dx, dy in directions:
                nextRow, nextCol = row + dx, col + dy
                if 0 <= nextRow < numRows and 0 <= nextCol < numCols and grid[nextRow][nextCol] == 1:
                    dfs(nextRow, nextCol)
        numRows, numCols = len(grid), len(grid[0])
        islandCount = 0
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 1:
                    islandCount += 1
                    dfs(row, col)
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 2:
                    grid[row][col] = 1
        return islandCount

    def minDays(self, grid: List[List[int]]) -> int:
        if self.countIslands(grid) != 1:
            return 0
        numRows, numCols = len(grid), len(grid[0])
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    if self.countIslands(grid) != 1:
                        return 1
                    grid[row][col] = 1
        return 2
