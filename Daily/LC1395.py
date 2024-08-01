from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for j in range (1, len(rating)-1):
            leftLess = 0
            leftGreater = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    leftLess += 1
                elif rating[i] > rating[j]:
                    leftGreater += 1
            rightLess = 0
            rightGreater = 0
            for k in range(j+1, len(rating)):
                if rating[k] < rating[j]:
                    rightLess += 1
                elif rating[k] > rating[j]:
                    rightGreater += 1
            ans += leftLess * rightGreater + leftGreater * rightLess
        return ans
