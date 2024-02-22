from math import inf
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        currentRow = matrix[0]
        for i in range(1, n):
            newRow = [0]*n
            for j in range(n):
                left = currentRow[j-1] if j > 0 else inf
                right = currentRow[j+1] if j < n-1 else inf
                newRow[j] = matrix[i][j] + min(left, right, currentRow[j])
            currentRow = newRow
        return min(currentRow)
