from itertools import pairwise

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum([abs(a-b) for a, b in pairwise([ord(c) for c in s])])
