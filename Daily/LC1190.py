class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        mapping = [0]*n
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                openIndex = stack.pop()
                mapping[i], mapping[openIndex] = openIndex, i
        i = 0
        direction = 1
        result = []
        while i < n:
            if s[i] in '()':
                i = mapping[i]
                direction = -direction
            else:
                result.append(s[i])
            i += direction
        return ''.join(result)
