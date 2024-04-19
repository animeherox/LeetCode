from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = []
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                diag.append((i+j, j, val))
        diag.sort()
        return [elem[2] for elem in diag]
