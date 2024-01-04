class Solution:
    def jump(self, nums: List[int]) -> int:
        endPos: int = len(nums)-1 # Avoid unnecessary repeated calls.
        currentPos: int = -1
        jumpCount: int = 0
        index: int = 0
        maxPos: int = 0
        while (maxPos < endPos):
            if (index > currentPos): # When we need to make a jump.
                currentPos = maxPos
                jumpCount += 1
            maxPos = max(maxPos, nums[index]+index)
            index += 1
        return jumpCount