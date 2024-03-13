class Solution:
    def countHomogenous(self, s: str) -> int:
        base = 10**9 + 7
        ans = count = 0
        current = ""
        for char in s:
            count = count + 1 if char == current else 1
            current = char
            ans += count
            ans %= base
        return ans
