from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        numFresh = timeElapsed = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numFresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        while queue and numFresh > 0:
            timeElapsed += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        numFresh -= 1
                        queue.append((x, y))
        return timeElapsed if numFresh == 0 else -1
