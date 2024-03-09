from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins, n, current = 0, len(arr), arr[0]
        for val in arr[1:]:
            if current < val:
                current = val
                wins = 1
            else:
                wins += 1
            if wins == k:
                return current
        return current
