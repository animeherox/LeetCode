class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for y in range(m):
                        if matrix[y][j] != 0:
                            matrix[y][j] = "."
                    for x in range(n):
                        if matrix[i][x] != 0:
                            matrix[i][x] = "."
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == ".":
                    matrix[i][j] = 0