from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        completedCount = 0
        graph = defaultdict(list)
        indegrees = [0]*numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
        # Initialize queue storing courses without incomplete prereqs
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        while queue:
            prereq = queue.popleft()
            completedCount += 1
            for course in graph[prereq]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return completedCount == numCourses
