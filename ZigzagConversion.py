class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = ['']*numRows
        downward = False
        currentRow = 0

        for letter in s:
            rows[currentRow] += letter
            if currentRow == 0 or currentRow == numRows-1:
                downward = not downward
            currentRow += 1 if downward else -1
        return ''.join(rows)