from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circleCount = 0
        squareCount = 0
        for student in students:
            if student == 1:
                squareCount += 1
            else:
                circleCount += 1
        for sandwich in sandwiches:
            if sandwich == 1:
                if squareCount == 0:
                    return circleCount
                squareCount -= 1
            else:
                if circleCount == 0:
                    return squareCount
                circleCount -= 1
        return 0
