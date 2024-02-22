class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        twoBack, oneBack, current = 0, 1, 1
        for _ in range(2, n):
            twoBack, oneBack, current = oneBack, current, twoBack+oneBack+current
        return current
