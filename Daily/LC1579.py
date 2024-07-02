from typing import List

class UnionFind:
    def __init__(self, size):
        # Initializes the UnionFind structure.
        # Each node is its own parent at first, and the size of each set is 1.
        # `count` tracks the number of disjoint sets.
        self.parent = list(range(size))
        self.set_size = [1] * size
        self.count = size

    def find(self, node):
        # Recursively finds the root parent of a node.
        # Applies path compression by linking the node directly to the root parent.
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Merges the sets of node1 and node2.
        # If they already share the same parent, no union is performed, returns False.
        # Otherwise, the smaller set is merged into the larger one, and True is returned.
        root1, root2 = self.find(node1 - 1), self.find(node2 - 1)
        if root1 == root2:
            return False
        if self.set_size[root1] > self.set_size[root2]:
            self.parent[root2] = root1
            self.set_size[root1] += self.set_size[root2]
        else:
            self.parent[root1] = root2
            self.set_size[root2] += self.set_size[root1]
        self.count -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        aliceUF = UnionFind(n)
        bobUF = UnionFind(n)
        numEdgesRemoved = 0
        for edgeType, node1, node2 in edges:
            if edgeType == 3:
                if not aliceUF.union(node1, node2):
                    numEdgesRemoved += 1
                else:
                    bobUF.union(node1, node2)
        for edgeType, node1, node2 in edges:
            if edgeType == 1:
                if not aliceUF.union(node1, node2):
                    numEdgesRemoved += 1
            elif edgeType == 2:
                if not bobUF.union(node1, node2):
                    numEdgesRemoved += 1
        if aliceUF.count == 1 and bobUF.count == 1:
            return numEdgesRemoved
        return -1
