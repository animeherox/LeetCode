class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        operations = [[float('inf')] * n for _ in range(n)]
        for start in range(n-1, -1, -1):
            operations[start][start] = 1
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    operations[start][end] = operations[start][end-1]
                else:
                    for pivot in range(start, end):
                        operations[start][end] = min(
                            operations[start][end],
                            operations[start][pivot] + operations[pivot+1][end]
                        )
        return operations[0][-1]
