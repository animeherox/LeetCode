from collections import Counter
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        distincts = 0
        for s in arr:
            if counts[s] == 1:
                distincts += 1
                if distincts == k:
                    return s
        return ""
