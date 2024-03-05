class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return right-left+1
            else:
                char = s[left]
                while left < len(s) and s[left] == char:
                    left += 1
                while right >= 0 and s[right] == char:
                    right -= 1
        return 1 if left == right else 0
