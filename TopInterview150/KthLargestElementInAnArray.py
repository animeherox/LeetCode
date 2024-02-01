class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(start, end, k_smallest):
            if start == end:
                return nums[start]
            mid = (start+end)//2
            mid_val = nums[mid]
            left, right = start-1, end+1
            while left < right:
                while True:
                    left += 1
                    if nums[left] >= mid_val:
                        break
                while True:
                    right -= 1
                    if nums[right] <= mid_val:
                        break
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
            if right < k_smallest:
                return quick_select(right+1, end, k_smallest)
            else:
                return quick_select(start, right, k_smallest)
        n = len(nums)
        k_smallest = n-k
        return quick_select(0, n-1, k_smallest)
