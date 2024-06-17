from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            currentSum = left**2 + right**2
            if currentSum == c:
                return True
            elif currentSum > c:
                right -= 1
            else:
                left += 1
        return False
