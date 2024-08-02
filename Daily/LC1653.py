class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        countB = 0
        for char in s:
            if char == 'b':
                countB += 1
            else:
                ans = min(ans+1, countB)
        return ans
