class Solution:
    def trap(self, height: List[int]) -> int:
        numBars = len(height)
        maxLeft = [height[0]]*numBars
        maxRight = [height[-1]]*numBars
        # Compute max heights to left and right of a given element
        for i in range(1, numBars):
            maxLeft[i] = max(maxLeft[i-1], height[i])
        for i in range(numBars-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
        # Compute trapped water, bar by bar
        trappedAmounts = [min(maxLeft[i], maxRight[i])-height[i] for i in range(numBars)]
        return sum(trappedAmounts)