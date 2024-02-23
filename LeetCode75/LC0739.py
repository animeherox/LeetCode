from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                previousIndex = stack.pop()
                answer[previousIndex] = i - previousIndex
            stack.append(i)
        return answer
