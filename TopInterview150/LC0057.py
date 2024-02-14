from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        mergedIntervals = [intervals[0]]
        for start, end in intervals[1:]:
            if mergedIntervals[-1][1] < start:
                mergedIntervals.append([start,end])
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], end)
        return mergedIntervals