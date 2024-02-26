from collections import Counter
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        numWords = len(words)
        counters = [Counter(word) for word in words]
        totalCounts = sum(counters, Counter())
        for count in totalCounts.values():
            if count % numWords != 0:
                return False
        return True
