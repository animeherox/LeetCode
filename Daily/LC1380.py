from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowMins = {min(row) for row in matrix}
        colMaxes = {max(col) for col in zip(*matrix)}
        return list(rowMins & colMaxes)
