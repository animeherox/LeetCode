class Solution:
    def climbStairs(self, n: int) -> int:
        previous, current = 0, 1
        for _ in range(n):
            previous, current = current, previous+current
        return current
