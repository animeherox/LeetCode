from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator, commonDenominator = 0, 2520 # LCM of 1..10
        if expression[0].isdigit():
            expression = '+' + expression
        i, length = 0, len(expression)
        while i < length:
            sign = -1 if expression[i] == '-' else 1
            i += 1
            j = i
            while j < length and expression[j] not in '-+':
                j += 1
            fractionStr = expression[i:j]
            numeratorStr, denominatorStr = fractionStr.split('/')
            numerator += sign * int(numeratorStr) * commonDenominator // int(denominatorStr)
            i = j
        divisor = gcd(numerator, commonDenominator)
        numerator //= divisor
        commonDenominator //= divisor
        return f'{numerator}/{commonDenominator}'
