class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = score = s[1:].count('1') + (0 if s[0] == '1' else 1)
        for digit in s[1:-1]:
            if digit == '0':
                score += 1
                maxScore = max(score, maxScore)
            else:
                score -= 1
        return maxScore
