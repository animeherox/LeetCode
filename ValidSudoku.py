class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First, validate the rows
        for i in range(9):
            rowSet = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in rowSet:
                    return False
                else:
                    rowSet.add(board[i][j])
        
        # Then validate the columns
        for i in range(9):
            columnSet = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in columnSet:
                    return False
                else:
                    columnSet.add(board[j][i])

        # Finally validate each of the 3x3 grids
        for x in range(3):
            for y in range(3):
                gridSet = set()
                for i in range(x*3, x*3+3):
                    for j in range(y*3, y*3+3):
                        if board[i][j] == '.':
                            continue
                        elif board[i][j] in gridSet:
                            return False
                        else:
                            gridSet.add(board[i][j])

        return True