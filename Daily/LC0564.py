class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num, length = int(n), len(n)
        candidates = {
            10**(length-1) - 1,
            10**length + 1
        }
        prefix = int(n[:(length + 1) // 2])
        for i in range(prefix-1, prefix+2):
            j = i if length % 2 == 0 else i // 10
            palindrome = i
            while j > 0:
                palindrome = palindrome * 10 + j % 10
                j //= 10
            candidates.add(palindrome)
        candidates.discard(num)
        closestPalindrome = -1
        for candidate in candidates:
            if (
                closestPalindrome == -1 or 
                abs(candidate-num) < abs(closestPalindrome-num) or
                abs(candidate-num) == abs(closestPalindrome-num) and candidate < closestPalindrome):
                closestPalindrome = candidate
        return str(closestPalindrome)
