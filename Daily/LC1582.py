from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rowSums = [0]*m
        colSums = [0]*n
        numSpecial = 0
        for i in range(m):
            for j in range(n):
                rowSums[i] += mat[i][j]
                colSums[j] += mat[i][j]
        for i in range(m):
            for j in range(n):
                if rowSums[i] == 1 and colSums[j] == 1 and mat[i][j] == 1:
                    numSpecial += 1
        return numSpecial
