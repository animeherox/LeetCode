class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = 0
        def dfs(row):
            if row == n:
                nonlocal solutions
                solutions += 1
                return
            for col in range(n):
                pos_diag = row+col
                neg_diag = row-col+n
                if cols[col] or diag[pos_diag] or anti_diag[neg_diag]:
                    continue # Skip invalid placements
                cols[col] = diag[pos_diag] = anti_diag[neg_diag] = True
                dfs(row + 1)
                cols[col] = diag[pos_diag] = anti_diag[neg_diag] = False
        cols = [False] * n
        diag = [False] * (2 * n)
        anti_diag = [False] * (2 * n)
        dfs(0)
        return solutions
