from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        for i in range(len(routes)):
            for route in routes[i]:
                graph[route].append(i)
        ans = 0
        queue = deque([source])
        visited = set()
        while queue:
            ans += 1
            for _ in range(len(queue)):
                for bus in graph[queue.popleft()]:
                    if bus in visited:
                        continue
                    visited.add(bus)
                    for nextRoute in routes[bus]:
                        if nextRoute == target:
                            return ans
                        queue.append(nextRoute)
        return -1
