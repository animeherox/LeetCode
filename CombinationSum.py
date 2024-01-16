class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        partial_combination = []
        combinations = []

        def dfs(index: int, current_sum: int):
            if current_sum == 0:
                combinations.append(partial_combination[:])
                return
            if index >= len(candidates) or current_sum < candidates[index]:
                return
            # Case without current candidate
            dfs(index+1, current_sum)
            # Case with current candidate
            partial_combination.append(candidates[index])
            dfs(index, current_sum-candidates[index])
            partial_combination.pop()
            return
        
        dfs(0, target)
        return combinations
