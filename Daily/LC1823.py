class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        winner = (k + self.findTheWinner(n-1, k)) % n
        return n if winner == 0 else winner
