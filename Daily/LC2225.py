from collections import Counter
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losses = Counter()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] += 1
        players = sorted(list(players))
        zeroLosers = [player for player in players if losses[player] == 0]
        oneLosers = [player for player in players if losses[player] == 1]
        return [zeroLosers, oneLosers]
