from bisect import bisect_right, bisect_left
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(start for start, _ in flowers)
        ends = sorted(end for _, end in flowers)
        bloomCounts = [bisect_right(starts, p) - bisect_left(ends, p) for p in people]
        return bloomCounts
