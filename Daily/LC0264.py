class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = [1]*n
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            next2 = uglyNumbers[i2] * 2
            next3 = uglyNumbers[i3] * 3
            next5 = uglyNumbers[i5] * 5
            uglyNumbers[i] = min(next2, next3, next5)
            if uglyNumbers[i] == next2:
                i2 += 1
            if uglyNumbers[i] == next3:
                i3 += 1
            if uglyNumbers[i] == next5:
                i5 += 1
        return uglyNumbers[n-1]
