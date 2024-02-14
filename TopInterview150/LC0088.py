from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if (n==0):
            return
        elif (m==0):
            for i in range(n):
                nums1[i] = nums2[i]
            return
        # Go from the back of both, place the largest element at end of nums1.
        index_1: int = m-1 # The current index for nums1
        index_2: int = n-1 # The current index for nums2
        index_place: int = m+n-1 # The current index for placement
        while (index_1 >= 0 and index_2 >= 0):
            if (nums1[index_1] > nums2[index_2]):
                nums1[index_place] = nums1[index_1]
                index_1 -= 1
            else:
                nums1[index_place] = nums2[index_2]
                index_2 -= 1
            index_place -= 1
        # If there are leftover elements in nums2, add them all.
        if (index_1== -1):
            for i in range(0, index_2+1):
                nums1[i] = nums2[i]
        # If there are leftover elements in nums1, we are done either way.
