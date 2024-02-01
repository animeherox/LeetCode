class Solution:
    def trailingZeroes(self, n: int) -> int:
        numZeroes = 0
        while n:
            n //=5
            numZeroes += n
        return numZeroes
