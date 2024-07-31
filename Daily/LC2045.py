from collections import deque
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n+1)]
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        queue = deque([(1,0)])
        minTime = [[float('inf')] * 2 for _ in range(n + 1)]
        minTime[1][0] = 0
        while queue:
            currentNode, prevTime = queue.popleft()
            numChangeSignal = prevTime // change
            waitTime = 0 if numChangeSignal % 2 == 0 else change - (prevTime % change)
            newTime = prevTime + waitTime + time
            for neighbor in graph[currentNode]:
                if newTime < minTime[neighbor][0]:
                    minTime[neighbor][0] = newTime
                    queue.append((neighbor, newTime))
                elif minTime[neighbor][0] < newTime < minTime[neighbor][1]:
                    if neighbor == n:
                        return newTime
                    minTime[neighbor][1] = newTime
                    queue.append((neighbor, newTime))
