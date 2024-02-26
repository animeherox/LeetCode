from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        sIndex, sLen = 0, len(s)
        gIndex, gLen = 0, len(g)
        happy = 0
        while sIndex < sLen and gIndex < gLen:
            if s[sIndex] >= g[gIndex]:
                happy += 1
                sIndex += 1
            gIndex += 1
        return happy
