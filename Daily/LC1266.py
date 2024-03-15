from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        lastPoint = points[0]
        for point in points[1:]:
            time += max(abs(point[0]-lastPoint[0]), abs(point[1]-lastPoint[1]))
            lastPoint = point
        return time
