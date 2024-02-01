class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Go from left and right, make sure conditions are met
        numChildren = len(ratings)
        leftCandies = [1]*numChildren
        rightCandies = [1]*numChildren

        # Calculate minimum candies going from the left
        for i in range(1, numChildren):
            if ratings[i] > ratings[i-1]:
                leftCandies[i] = leftCandies[i-1] + 1

        # Calculate minimum candies going from the right
        for i in range(numChildren-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rightCandies[i] = rightCandies[i+1] + 1
        
        # Take maxima to find minimum candies overall
        candies = [max(left, right) for left, right in zip(leftCandies, rightCandies)]
        return sum(candies)