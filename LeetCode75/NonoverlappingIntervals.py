from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: interval[1])
        removedIntervals = 0
        endTime = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= endTime:
                endTime = end
            else:
                removedIntervals += 1
        return removedIntervals
