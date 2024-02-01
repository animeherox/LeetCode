class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and multiples of 10 other than 0 cannot be palindromes
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        x_reverse = 0
        while x_reverse < x:
            x_reverse = x_reverse * 10 + x % 10
            x //= 10
        return x == x_reverse or x == x_reverse // 10
