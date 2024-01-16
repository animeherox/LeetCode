class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result, operator = 0, 1
        index, length = 0, len(s)
        while index < length:
            if s[index].isdigit():
                number = 0
                while index < length and s[index].isdigit():
                    number = number*10 + int(s[index])
                    index += 1
                result += operator * number
                index -= 1
            elif s[index] == '+':
                operator = 1
            elif s[index] == '-':
                operator = -1
            elif s[index] == '(':
                stack.append(result)
                stack.append(operator)
                result, operator = 0, 1
            elif s[index] == ')':
                result *= stack.pop()
                result += stack.pop()
            index += 1
        return result