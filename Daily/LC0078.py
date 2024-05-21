from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index: int):
            if index == len(nums):
                ans.append(currentSubset[:])
                return
            dfs(index+1)
            currentSubset.append(nums[index])
            dfs(index+1)
            currentSubset.pop()
        ans = []
        currentSubset = []
        dfs(0)
        return ans
