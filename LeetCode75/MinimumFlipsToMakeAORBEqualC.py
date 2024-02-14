class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        min_flips = 0
        for i in range(30):
            bit_a = a >> i & 1
            bit_b = b >> i & 1
            bit_c = c >> i & 1
            if bit_a | bit_b != bit_c:
                if bit_a == 1 and bit_b == 1:
                    min_flips += 2
                else:
                    min_flips += 1
        return min_flips
