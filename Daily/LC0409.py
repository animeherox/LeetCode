from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = Counter(s)
        ans = 0
        oddFound = False
        for count in charCount.values():
            ans += (count // 2) * 2
            if not oddFound and count % 2 == 1:
                oddFound = True
        if oddFound:
            ans += 1
        return ans
