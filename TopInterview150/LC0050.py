class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPower(base: float, exponent: int) -> float:
            result = 1.0
            while exponent:
                # If exponent is odd, multiply by base once
                if exponent & 1:
                    result *= base
                # Square the base
                base *= base
                # Divide exponent by 2 (rounded down)
                exponent >>= 1
            return result
        return fastPower(x, n) if n >= 0 else 1 / fastPower(x, -n)