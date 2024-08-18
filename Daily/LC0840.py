from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(x: int, y: int) -> bool:
            uniqueVals = set()
            rowSums = [0]*3
            colSums = [0]*3
            diagSumLr = 0
            diagSumRl = 0
            for i in range(x, x+3):
                for j in range(y, y+3):
                    val = grid[i][j]
                    if val < 1 or val > 9:
                        return False
                    if val in uniqueVals:
                        return False
                    uniqueVals.add(val)
                    rowSums[i-x] += val
                    colSums[j-y] += val
                    if i-x == j-y:
                        diagSumLr += val
                    if i-x == 2 - (j-y):
                        diagSumRl += val
            if diagSumLr != diagSumRl:
                return False
            if any(rowSum != diagSumLr for rowSum in rowSums):
                return False
            if any(colSum != diagSumLr for colSum in colSums):
                return False
            return True
        rowCount, colCount = len(grid), len(grid[0])
        magicSquareCount = 0
        for i in range(rowCount-2):
            for j in range(colCount-2):
                magicSquareCount += isMagicSquare(i, j)
        return magicSquareCount
