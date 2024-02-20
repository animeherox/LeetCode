class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        prevRow = [1] + [0 for _ in range(k)]
        for j in range(1, n):
            currentRow = [1] + [0 for _ in range(k)]
            tmp = 1
            for i in range(1, k+1):
                tmp += prevRow[i]
                if i >= j+1:
                    tmp -= prevRow[i-j-1] 
                currentRow[i] = tmp
            prevRow = currentRow
        return prevRow[-1] % (10**9+7)