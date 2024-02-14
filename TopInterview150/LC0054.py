from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row, col, direction = 0, 0, 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0)) # RDLU
        visited = set()
        output = []
        for _ in range(m*n):
            output.append(matrix[row][col])
            visited.add((row,col))
            
            # Check if we need to turn direction
            nextRow, nextCol = row+directions[direction][0], col+directions[direction][1]
            if not (0 <= nextRow < m) or not (0 <= nextCol < n) or (nextRow, nextCol) in visited:
                direction = (direction+1)%4
            
            row += directions[direction][0]
            col += directions[direction][1]
        return output