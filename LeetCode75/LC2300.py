from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def firstSuccessIndex(spell: int) -> int:
            left, right = 0, m
            while left < right:
                mid = (left+right)//2
                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid+1
            return left
        potions.sort()
        m = len(potions)
        return [m - firstSuccessIndex(spell) for spell in spells]
