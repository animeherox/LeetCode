class Solution:
    def findComplement(self, num: int) -> int:
        binLength = len(bin(num)) - 2
        mask = (2 ** binLength) - 1
        return num ^ mask
