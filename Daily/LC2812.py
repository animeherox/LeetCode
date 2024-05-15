from collections import deque
from typing import List

class UnionFind:
    """A class that implements the Union-Find (Disjoint Set) data structure."""
    def __init__(self, size):
        # Parent pointers initialised to point to themselves and sizes initialised to 1
        self.parent = list(range(size))
        self.set_size = [1] * size

    def find(self, x):
        """Finds the representative (root) of the set containing 'x'. Implements path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        """Unites the sets containing 'a' and 'b'. Return False if they are already in the same set, True otherwise."""
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        # Union by size, making the smaller root point to the larger one
        if self.set_size[root_a] > self.set_size[root_b]:
            self.parent[root_b] = root_a
            self.set_size[root_a] += self.set_size[root_b]
        else:
            self.parent[root_a] = root_b
            self.set_size[root_b] += self.set_size[root_a]
        return True

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return 0
        queue = deque()
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i,j))
                    dist[i][j] = 0
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < n and dist[x][y] == float('inf'):
                    dist[x][y] = dist[i][j] + 1
                    queue.append((x,y))
        candidates = sorted(((dist[i][j], i, j) for i in range(n) for j in range(n)), reverse=True)
        uf = UnionFind(n * n)
        for d, i, j in candidates:
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < n and dist[x][y] >= d:
                    uf.union(i * n + j, x * n + y)
            if uf.find(0) == uf.find(n * n - 1):
                return d
        return 0
