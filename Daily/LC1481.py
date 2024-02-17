from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        counts = sorted(counter.values())
        for i, value in enumerate(counts):
            k -= value
            if k < 0:
                return len(counter) - i
        return 0