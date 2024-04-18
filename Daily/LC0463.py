from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    ans += 4
                    if row < rows-1 and grid[row+1][col] == 1:
                        ans -= 2
                    if col < cols-1 and grid[row][col+1] == 1:
                        ans -= 2
        return ans
