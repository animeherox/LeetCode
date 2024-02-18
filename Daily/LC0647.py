class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def palindromeSearch(l: int, r: int):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            palindromeSearch(i, i)
            palindromeSearch(i, i+1)
        return count