from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPos: int = 0
        for pos in range(len(nums)):
            if (pos>maxPos): # If we hit an unreachable position, we can't jump.
                return False
            maxPos = max(maxPos, pos+nums[pos])
        return True # If we make it to the end without jumping, we've succeeded.