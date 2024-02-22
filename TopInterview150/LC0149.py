from collections import Counter
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        max_points = 1

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        for i in range(num_points):
            x1, y1 = points[i]
            slopes = Counter()
            for j in range(i+1, num_points):
                # Calculate slope
                x2, y2 = points[j]
                dx = x2-x1
                dy = y2-y1
                gcd_value = gcd(dx, dy)
                slope = (dx//gcd_value, dy//gcd_value)

                # Process number of points on line as candidate
                slopes[slope] += 1
                max_points = max(max_points, slopes[slope] + 1) # Add 1 for points[i]
        
        return max_points
