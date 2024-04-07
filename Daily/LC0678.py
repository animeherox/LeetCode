class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount = 0
        for char in s:
            if char in '(*':
                openCount += 1
            elif openCount:
                openCount -= 1
            else:
                return False
        openCount = 0
        for char in reversed(s):
            if char in '*)':
                openCount += 1
            elif openCount:
                openCount -= 1
            else:
                return False
        return True
