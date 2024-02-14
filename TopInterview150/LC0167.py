from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startIndex, endIndex = 0, len(numbers)-1
        while (startIndex<endIndex):
            current = numbers[startIndex]+numbers[endIndex]
            if current == target:
                return [startIndex+1, endIndex+1] # Add 1 to 1-index
            elif current < target:
                startIndex += 1
            else:
                endIndex -= 1
        print("No solution found.")