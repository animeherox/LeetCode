from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        minPushes = 0
        sortedCounts = sorted(counts.values(), reverse=True)
        for i, count in enumerate(sortedCounts):
            minPushes += ((i//8)+1) * count
        return minPushes
