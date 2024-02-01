class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live_neighbors = -board[i][j]
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0 <= x < m and 0 <= y < n and board[x][y] > 0:
                            live_neighbors += 1
                if board[i][j] and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 2 # Mark as live, but soon to die
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = -1 # Mark as dead, but soon to live
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
