from collections import Counter
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numFreqs = Counter(nums)
        result = []
        for num, freq in numFreqs.items():
            for i in range(freq):
                if len(result) > i:
                    result[i].append(num)
                else:
                    result.append([num])
        return result
