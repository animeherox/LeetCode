# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binarySearch(left: int, right: int, direction: int) -> int:
            while left < right:
                mid = (left + right) // 2
                if direction * mountain_arr.get(mid) >= direction * target:
                    right = mid
                else:
                    left = mid + 1
            if mountain_arr.get(left) == target:
                return left
            else:
                return -1
        # First, find the peak
        n = mountain_arr.length()
        left, right = 0, n-1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                right = mid
            else:
                left = mid+1
        peak = left
        # Search the left side
        result = binarySearch(0, peak, 1)
        if result == -1:
            result = binarySearch(peak+1, n-1, -1)
        return result
