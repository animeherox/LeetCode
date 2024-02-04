from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        combination = []
        def dfs(start, target):
            if target == 0 and len(combination) == k:
                # Case 1: We have found a solution
                results.append(combination[:])
                return
            if start > 9 or start > target or len(combination) >= k:
                # Case 2: No possible solutions exist from current state
                return
            combination.append(start)
            dfs(start+1, target-start)
            combination.pop()
            dfs(start+1, target)
        dfs(1, n)
        return results
