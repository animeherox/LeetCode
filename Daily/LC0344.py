from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for l in range(n//2):
            r = n - l - 1
            s[l], s[r] = s[r], s[l]
