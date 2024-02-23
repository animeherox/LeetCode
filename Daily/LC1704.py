class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        countBalance = 0
        n = len(s)
        for char in s[:n//2]:
            if char in vowels:
                countBalance += 1
        for char in s[n//2:]:
            if char in vowels:
                countBalance -= 1
        return countBalance == 0
