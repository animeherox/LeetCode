from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        tCount = Counter(t)
        diff = 0
        for sChar in sCount:
            diff += abs(sCount[sChar] - tCount[sChar])
        for tChar, tVal in tCount.items():
            if tChar not in sCount:
                diff += tVal
        return diff//2
