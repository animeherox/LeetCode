class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        left, right = 0, len(s) - 1
        sList = list(s)
        while left < right:
            while left < right and sList[left] not in vowels:
                left += 1
            while left < right and sList[right] not in vowels:
                right -= 1
            if left < right:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
        return ''.join(sList)
