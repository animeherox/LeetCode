from heapq import heappop, heappush
from typing import List

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]):
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        dists = [float('inf')] * self.n
        dists[node1] = 0
        minHeap = [(dists[node1], node1)]
        while minHeap:
            dist, currentNode = heappop(minHeap)
            if currentNode == node2:
                return dist
            for newNode, cost in self.graph[currentNode]:
                if dist + cost < dists[newNode]:
                    dists[newNode] = dist + cost
                    heappush(minHeap, (dists[newNode], newNode))
        return -1
