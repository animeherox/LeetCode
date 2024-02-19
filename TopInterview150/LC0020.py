class Solution:
    def isValid(self, s: str) -> bool:
        closeMap = {')':'(', '}':'{', ']':'['}
        openStack = []
        for char in s:
            if char in closeMap:
                if openStack == [] or closeMap[char] != openStack.pop():
                    return False
            else:
                openStack.append(char)
        return len(openStack) == 0
