class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp_table = [[0] * n for _ in range(m)]

        # Populate first row and column
        if obstacleGrid[0][0] == 0:
            dp_table[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp_table[i][0] = dp_table[i-1][0]
            else:
                break
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp_table[0][j] = dp_table[0][j-1]
            else:
                break

        # Fill in the rest
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp_table[i][j] = dp_table[i][j-1] + dp_table[i-1][j]
        return dp_table[m-1][n-1]