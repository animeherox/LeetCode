class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        num_arrows, last_arrow_pos = 0, -float('inf')
        # Sort by end for greedy algorithm
        sorted_points = sorted(points, key=lambda x: x[1])
        for start, end in sorted_points:
            if start > last_arrow_pos:
                num_arrows += 1
                last_arrow_pos = end
        return num_arrows
