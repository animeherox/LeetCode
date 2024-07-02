from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive = 0
        for n in arr:
            if n % 2 == 1:
                consecutive += 1
                if consecutive == 3:
                    return True
            else:
                consecutive = 0
        return False
