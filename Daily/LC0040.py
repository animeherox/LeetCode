from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(startIndex: int, remainder: int):
            if remainder == 0:
                combinations.append(combination[:])
                return
            if startIndex >= len(candidates) or remainder < candidates[startIndex]:
                return
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i-1]:
                    continue
                combination.append(candidates[i])
                dfs(i+1, remainder-candidates[i])
                combination.pop()
        candidates.sort()
        combinations = []
        combination = []
        dfs(0, target)
        return combinations
