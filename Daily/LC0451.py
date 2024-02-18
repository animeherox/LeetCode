from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = Counter(s)
        sortedFreqs = sorted(freqs.items(), key=lambda item: -item[1])
        ans = ''.join(freq[0]*freq[1] for freq in sortedFreqs)
        return ans
