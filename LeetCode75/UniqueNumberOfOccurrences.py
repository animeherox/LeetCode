from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrCounter = Counter(arr)
        occurrences = set(arrCounter.values())
        return len(arrCounter) == len(occurrences)
