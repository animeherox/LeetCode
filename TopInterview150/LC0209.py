from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, lenN, total, best = 0, 0, len(nums), 0, float("inf")
        while (j < lenN):
            total += nums[j]
            while i <= j:
                if (total >= target): # If over target, shrink from the left
                    best = min(best, j+1-i)
                    total -= nums[i]
                    i += 1
                else:
                    break
            j += 1 # Once we dip below the target, expand to the right
        if best == float("inf"):
            return 0
        else:
            return best
