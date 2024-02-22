from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthElement(index1: int, index2: int, k: int) -> int:
            if index1 >= length1:
                return nums2[index2 + k - 1]
            elif index2 >= length2:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            # Compare halfway points, and search halves accordingly
            half_k = k//2
            midVal1 = nums1[index1 + half_k - 1] if index1 + half_k - 1 < length1 else float('inf')
            midVal2 = nums2[index2 + half_k - 1] if index2 + half_k - 1 < length2 else float('inf')

            if midVal1 < midVal2:
                return findKthElement(index1 + half_k, index2, k - half_k)
            else:
                return findKthElement(index1, index2 + half_k, k - half_k)
        
        length1, length2 = len(nums1), len(nums2)
        leftMedian = findKthElement(0, 0, (length1+length2+1)//2)
        rightMedian = findKthElement(0, 0, (length1+length2+2)//2)
        return (leftMedian+rightMedian)/2
