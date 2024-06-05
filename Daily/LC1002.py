from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
        for word in words[1:]:
            newCounts = Counter(word)
            for c in counts:
                counts[c] = min(counts[c], newCounts[c])
        result = []
        for c in counts:
            result += [c]*counts[c]
        return result
