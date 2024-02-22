from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        permutations = []
        for i in range(len(nums)):
            permutations += [[nums[i]]+partial for partial in self.permute(nums[:i]+nums[i+1:])]
        return permutations