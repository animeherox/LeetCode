from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = maxScore = 0
        left, right = 0, len(tokens)-1
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                left += 1
                score += 1
                maxScore = max(maxScore, score)
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return maxScore
