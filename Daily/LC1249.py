class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openCount = 0
        stack = []
        for c in s:
            if c == ')' and openCount == 0:
                continue
            if c == '(':
                openCount += 1
            elif c == ')':
                openCount -= 1
            stack.append(c)
        openCount = 0
        ans = []
        for c in reversed(stack):
            if c == '(' and openCount == 0:
                continue
            if c == ')':
                openCount += 1
            elif c == '(':
                openCount -= 1
            ans.append(c)
        return ''.join(reversed(ans))
