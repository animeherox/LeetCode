from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for start in range(1, 9):
            current = start
            for digit in range(start+1, 10):
                current = current * 10 + digit
                if low <= current <= high:
                    ans.append(current)
        return sorted(ans)
