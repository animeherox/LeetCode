class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstOcc = {}
        maxLength = -1
        for i, char in enumerate(s):
            if char in firstOcc:
                maxLength = max(maxLength, i-firstOcc[char]-1)
            else:
                firstOcc[char] = i
        return maxLength
