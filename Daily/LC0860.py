from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = [0]*2
        for bill in bills:
            if bill == 5:
                counts[0] += 1
            elif bill == 10:
                counts[0] -= 1
                counts[1] += 1
            else:
                if counts[1] > 0:
                    counts[0] -= 1
                    counts[1] -= 1
                else:
                    counts[0] -= 3
            if counts[0] < 0:
                return False
        return True
