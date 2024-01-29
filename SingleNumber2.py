class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = twice = 0
        for n in nums:
            once_new = (~once & twice & n) | (once & ~twice & ~n)
            twice_new = ~once & (twice ^ n)
            once, twice = once_new, twice_new
        return twice
