from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n
        while start<end:
            mid = (start+end)//2
            i,j = divmod(mid,n)
            value = matrix[i][j]
            if value == target:
                return True
            elif value < target:
                start = mid + 1
            else:
                end = mid
        i,j = divmod(mid,n)
        return matrix[i][j]==target