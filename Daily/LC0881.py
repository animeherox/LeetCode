from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        lightIndex, heavyIndex = 0, len(people)-1
        while lightIndex <= heavyIndex:
            if people[lightIndex] + people[heavyIndex] <= limit:
                lightIndex += 1
            heavyIndex -= 1
            count += 1
        return count