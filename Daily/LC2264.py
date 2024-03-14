class Solution:
    def largestGoodInteger(self, num: str) -> str:
        bestDigit = -1
        num = [int(n) for n in num]
        for i in range(len(num)-2):
            digit = num[i]
            if digit > bestDigit:
                if num[i+1] == digit:
                    if num[i+2] == digit:
                        bestDigit = digit
                    else:
                        i += 1
        return "" if bestDigit == -1 else str(bestDigit)*3
