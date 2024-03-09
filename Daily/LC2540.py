from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index1 = index2 = 0
        len1, len2 = len(nums1), len(nums2)
        while index1 < len1 and index2 < len2:
            if nums1[index1] == nums2[index2]:
                return nums1[index1]
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                index1 += 1
        return -1
