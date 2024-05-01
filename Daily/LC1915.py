from collections import Counter

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        maskCount = Counter({0:1})
        wonderfulCount = 0
        currentMask = 0
        for c in word:
            currentMask ^= 1 << (ord(c) - ord('a'))
            wonderfulCount += maskCount[currentMask]
            for i in range(10):
                wonderfulCount += maskCount[currentMask ^ (1 << i)]
            maskCount[currentMask] += 1
        return wonderfulCount
