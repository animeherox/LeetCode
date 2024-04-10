from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        for card in sorted(deck, reverse=True):
            queue.rotate()
            queue.appendleft(card)
        return list(queue)
