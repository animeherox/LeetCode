from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        rows, cols = len(grid), len(grid[0])
        def dfs(row, col):
            '''
            Given a row and column, perform a DFS to adjacent land, marking all
            as water, which we can treat as equivalent to searched land.
            '''
            grid[row][col] = "0"
            for dx,dy in directions:
                newRow, newCol = row+dx, col+dy
                if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == "1":
                    dfs(newRow, newCol)
        
        numIslands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    numIslands += 1
        
        return numIslands