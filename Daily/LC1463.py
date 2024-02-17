from itertools import product
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        currentRowDp = [[-1] * cols for _ in range(cols)]
        nextRowDp = [[-1] * cols for _ in range(cols)]
        currentRowDp[0][cols - 1] = grid[0][0] + grid[0][cols - 1]
        for row in range(1, rows):
            for j1 in range(cols):
                for j2 in range(cols):
                    pickup = grid[row][j1] + (0 if j1 == j2 else grid[row][j2])
                    for y1 in range(max(j1-1, 0), min(j1+2, cols)):
                        for y2 in range(max(j2-1, 0), min(j2+2, cols)):
                            if currentRowDp[y1][y2] != -1: # Skip unreachable states
                                nextRowDp[j1][j2] = max(nextRowDp[j1][j2], currentRowDp[y1][y2]+pickup)
            currentRowDp, nextRowDp = nextRowDp, [[-1] * cols for _ in range(cols)]
        return max([currentRowDp[j1][j2] for j1, j2 in product(range(cols), range(cols))])
