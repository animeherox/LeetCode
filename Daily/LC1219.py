from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n and grid[x][y]):
                return 0
            gold = grid[x][y]
            grid[x][y] = 0
            totalGold = gold + max(
                dfs(x+dx, y+dy) for dx, dy in directions
            )
            grid[x][y] = gold
            return totalGold
        return max(dfs(i, j) for i in range(m) for j in range(n))
