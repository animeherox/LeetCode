from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def findRoot(rootId):
            if parent[rootId] != rootId:
                parent[rootId] = findRoot(parent[rootId])
            return parent[rootId]
        numNodes = 10001
        parent = list(range(numNodes * 2))
        for x, y in stones:
            parent[findRoot(x)] = findRoot(y + numNodes)
        uniqueRoots = {findRoot(x) for x, _ in stones}
        return len(stones) - len(uniqueRoots)
