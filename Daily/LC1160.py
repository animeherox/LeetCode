from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCounts = Counter(chars)
        total = 0
        for word in words:
            wordCounts = Counter(word)
            isValid = True
            for char in wordCounts:
                if wordCounts[char] > charCounts[char]:
                    isValid = False
                    break
            if isValid:
                total += len(word)
        return total
