from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def findSet(rootIndex):
            if parent[rootIndex] != rootIndex:
                parent[rootIndex] = findSet(parent[rootIndex])
            return parent[rootIndex]
        
        def unionSets(setA, setB):
            rootA, rootB = findSet(setA), findSet(setB)
            if rootA != rootB:
                parent[rootA] = rootB
                nonlocal regionCount
                regionCount -= 1
        
        n = len(grid)
        regionCount = n * n * 4
        parent = list(range(regionCount))
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                cellIndex = i * n + j
                # If not in the bottom row, unite bottom and top of adjacent cells
                if i < n - 1:
                    unionSets(4 * cellIndex + 2, 4 * (cellIndex + n))
                # If not in the rightmost column, unite right and left of adjacent cells
                if j < n - 1:
                    unionSets(4 * cellIndex + 1, 4 * (cellIndex + 1) + 3)
                
                if val == '/':
                    unionSets(4 * cellIndex, 4 * cellIndex + 3)
                    unionSets(4 * cellIndex + 1, 4 * cellIndex + 2)
                elif val == '\\':
                    unionSets(4 * cellIndex, 4 * cellIndex + 1)
                    unionSets(4 * cellIndex + 2, 4 * cellIndex + 3)
                else:
                    unionSets(4 * cellIndex, 4 * cellIndex + 1)
                    unionSets(4 * cellIndex + 1, 4 * cellIndex + 2)
                    unionSets(4 * cellIndex + 2, 4 * cellIndex + 3)
        return regionCount
