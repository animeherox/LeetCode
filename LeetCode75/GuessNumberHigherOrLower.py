class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while high > low:
            mid = (low + high)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                low = mid+1
            elif result == -1:
                high = mid-1
        return low
