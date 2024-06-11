from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        count = [0] * 1001
        for n in arr1:
            count[n] += 1
        for n in arr2:
            while count[n] > 0:
                ans.append(n)
                count[n] -= 1
        for n in range(1001):
            for _ in range(count[n]):
                ans.append(n)
        return ans

