from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseOrder = []
        graph = defaultdict(list)
        indegrees = [0]*numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        while queue:
            prereq = queue.popleft()
            courseOrder.append(prereq)
            for course in graph[prereq]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return courseOrder if len(courseOrder) == numCourses else []