from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(board), len(board[0])
        def dfs_search(x: int, y: int, index: int) -> bool:
            # Handle case where we reach the end
            if index == len(word) - 1:
                return board[x][y] == word[index]
            # If we hit a mismatch, abandon the path
            if board[x][y] != word[index]:
                return False
            # Temporarily mark board position as visited
            temp = board[x][y]
            board[x][y] = "."
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] != ".":
                    # Stop early when we find a solution
                    if dfs_search(new_x, new_y, index + 1):
                        return True
            # Unmark board position as visited
            board[x][y] = temp
            return False
        for i in range(m):
            for j in range(n):
                # Stop early when we find a solution
                if board[i][j] == word[0] and dfs_search(i, j, 0):
                    return True
        return False
