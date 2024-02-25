from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lastCount = totalBeams = 0
        for row in bank:
            currentCount = row.count('1')
            if currentCount > 0:
                totalBeams += lastCount * currentCount
                lastCount = currentCount
        return totalBeams
