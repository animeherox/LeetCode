class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [1]*n
        for _ in range(1, m):
            for y in range(1, n):
                paths[y] += paths[y-1]
        return paths[-1]
