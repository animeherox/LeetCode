from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0]*n
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1
        leavesQueue = deque(i for i in range(n) if degree[i] == 1)
        minHeightTrees = []
        while leavesQueue:
            minHeightTrees.clear()
            for _ in range(len(leavesQueue)):
                currentNode = leavesQueue.popleft()
                minHeightTrees.append(currentNode)
                for neighbor in graph[currentNode]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leavesQueue.append(neighbor)
        return minHeightTrees