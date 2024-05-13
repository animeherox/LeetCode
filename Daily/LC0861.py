from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        ans = 0
        for j in range(n):
            numOnes = sum(grid[i][j] for i in range(m))
            ans += max(numOnes, m-numOnes) * (1 << n-j-1)
        return ans
