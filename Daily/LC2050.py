from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        prereqCounts = [0]*n
        for start, end in relations:
            graph[start-1].append(end-1)
            prereqCounts[end-1] += 1
        queue = deque()
        endTimes = [0]*n
        for i, (prereqCount, duration) in enumerate(zip(prereqCounts, time)):
            if prereqCount == 0:
                endTimes[i] = duration
                queue.append(i)
        while queue:
            for _ in range(len(queue)):
                currentCourse = queue.popleft()
                for nextCourse in graph[currentCourse]:
                    endTimes[nextCourse] = max(endTimes[nextCourse], endTimes[currentCourse]+time[nextCourse])
                    prereqCounts[nextCourse] -= 1
                    if prereqCounts[nextCourse] == 0:
                        queue.append(nextCourse)
        return max(endTimes)
