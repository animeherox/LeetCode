from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cardCount = Counter(hand)
        for value in sorted(hand):
            if cardCount[value]:
                for nextValue in range(value, value+groupSize):
                    if cardCount[nextValue] == 0:
                        return False
                    cardCount[nextValue] -= 1
        return True
