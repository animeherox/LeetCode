from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def squareToCoordinates(squareNumber: int) -> tuple[int, int]:
            row, col = divmod(squareNumber-1, n)
            if row % 2 == 1:
                col = n-1 - col
            return n-1 - row, col
        n = len(board)
        queue = deque([1])
        visited = {1} # Track visited squares to avoid loops
        steps = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == n*n:
                    return steps
                for next_square in range(current + 1, min(current + 7, n * n + 1)):
                    i, j = squareToCoordinates(next_square)
                    if board[i][j] != -1:
                        # We must take any snakes/ladders
                        next_square = board[i][j]
                    if next_square not in visited:
                        visited.add(next_square)
                        queue.append(next_square)
            steps += 1
        # We only reach here if all paths are exhausted
        return -1
