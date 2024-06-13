from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = sum(abs(seat-student) for seat, student in zip(seats, students))
        return moves
