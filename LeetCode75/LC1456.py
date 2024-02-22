class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        fast, slow = 0, 0
        length = len(s)
        vowelCount = 0
        for _ in range(k):
            if s[fast] in vowels:
                vowelCount += 1
            fast += 1
        maxVowels = vowelCount
        while fast < length:
            if s[fast] in vowels:
                vowelCount += 1
            if s[slow] in vowels:
                vowelCount -= 1
            fast += 1
            slow += 1
            maxVowels = max(maxVowels, vowelCount)
        return maxVowels
