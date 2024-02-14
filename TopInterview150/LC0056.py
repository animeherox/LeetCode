from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedIntervals = [intervals[0]]
        for start, end in intervals[1:]:
            if mergedIntervals[-1][1] < start:
                mergedIntervals.append([start,end])
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], end)
        return mergedIntervals