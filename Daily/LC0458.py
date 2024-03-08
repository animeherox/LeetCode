from math import ceil, log

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        base = minutesToTest // minutesToDie + 1
        return ceil(log(buckets-0.01, base)) # Slightly reduce for float error