class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1, flip the matrix upside down
        n = len(matrix)
        for i in range(n//2):
            opposite = n-i-1
            temp = matrix[i]
            matrix[i] = matrix[opposite]
            matrix[opposite] = temp
        # Step 2, reflect along diagonal
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp