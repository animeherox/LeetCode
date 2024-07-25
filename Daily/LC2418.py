from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [person[1] for person in reversed(sorted(zip(heights, names)))]
