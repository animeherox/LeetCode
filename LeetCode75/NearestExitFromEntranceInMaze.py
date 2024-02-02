from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        i, j = entrance
        queue = deque([(i,j)])
        maze[i][j] = '+' # Mark visited cells as equivalent to walls
        stepCounter = 0
        while queue:
            stepCounter += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    x, y = i+dx, j+dy
                    if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            return stepCounter
                        queue.append((x,y))
                        maze[x][y] = '+'
        # We only reach here if all paths have been exhausted
        return -1
