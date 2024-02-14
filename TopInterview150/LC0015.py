from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        i = 0
        while i < len(nums)-2:
            oldI = nums[i]
            target = -oldI
            j = i+1 # LeftPtr from 2Sum
            k = len(nums)-1 # RightPtr from 2Sum
            while (j<k):
                current = nums[j] + nums[k]
                if current == target:
                    triplets.append([oldI,nums[j],nums[k]])
                    oldJ = nums[j]
                    while nums[j] == oldJ and j<k: # Avoid duplicates
                        j += 1
                elif current < target:
                    oldJ = nums[j]
                    while nums[j] == oldJ and j<k: # Avoid duplicates
                        j += 1
                else:
                    oldK = nums[k]
                    while nums[k] == oldK and j<k: # Avoid duplicates
                        k -= 1
            while nums[i] == oldI and i < len(nums)-2: # Avoid duplicates
                i += 1
        return triplets