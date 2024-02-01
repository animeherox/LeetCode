class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystackLength, needleLength = len(haystack), len(needle)
        for i in range(haystackLength-needleLength+1):
            if haystack[i] == needle[0]:
                matchFound = True
                for j in range(1, needleLength):
                    if haystack[i+j] != needle[j]:
                        matchFound = False
                        break
                if matchFound:
                    return i
        return -1