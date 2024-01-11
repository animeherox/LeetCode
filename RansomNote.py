from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        for letter in ransomCount:
            if magazineCount[letter] < ransomCount[letter]:
                return False
        return True