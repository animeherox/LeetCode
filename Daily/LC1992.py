from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 or i > 0 and land[i-1][j] == 1 or j > 0 and land[i][j-1] == 1:
                    continue
                end_i, end_j = i, j
                while end_i + 1 < m and land[end_i+1][j] == 1:
                    end_i += 1
                while end_j + 1 < n and land[i][end_j+1] == 1:
                    end_j += 1
                ans.append([i, j, end_i, end_j])
        return ans
