from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed_grid = [list(column) for column in zip(*grid)]
        answer = 0
        for row in grid:
            for transposed_row in transposed_grid:
                if row == transposed_row:
                    answer += 1
        return answer
