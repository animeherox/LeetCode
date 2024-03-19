from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = Counter(tasks)
        maxFreq = max(taskCounts.values())
        maxFreqCount = sum(freq == maxFreq for freq in taskCounts.values())
        idleTime = (maxFreq - 1) * (n + 1)
        minLength = idleTime + maxFreqCount
        return max(minLength, len(tasks))
