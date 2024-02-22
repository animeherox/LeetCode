class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        base = 10**9 + 7
        ans = 0
        paths = [[0] * n for _ in range(m)]
        paths[startRow][startColumn] = 1
        for _ in range(maxMove):
            newPaths = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if paths[i][j] > 0:
                        for dx, dy in dirs:
                            x = i+dx
                            y = j+dy
                            if 0 <= x < m and 0 <= y < n:
                                newPaths[x][y] = (newPaths[x][y] + paths[i][j]) % base
                            else:
                                ans = (ans + paths[i][j]) % base
            paths = newPaths
        return ans % base
