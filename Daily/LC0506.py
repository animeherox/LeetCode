from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        points = [(val, i) for i, val in enumerate(score)]
        points.sort()
        for i, scorePair in enumerate(reversed(points)):
            if i >= 3:
                score[scorePair[1]] = str(i+1)
            elif i == 0:
                score[scorePair[1]] = "Gold Medal"
            elif i == 1:
                score[scorePair[1]] = "Silver Medal"
            elif i == 2:
                score[scorePair[1]] = "Bronze Medal"
        return score
