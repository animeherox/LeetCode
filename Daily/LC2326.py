from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        row, col = 0, 0
        direction = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while head:
            matrix[row][col] = head.val
            head = head.next
            nextRow, nextCol = row + directions[direction][0], col + directions[direction][1]
            if (nextRow < 0 or nextCol < 0 or
                nextRow >= m or nextCol >= n or
                matrix[nextRow][nextCol] != -1):
                direction = (direction + 1) % 4
                nextRow, nextCol = row + directions[direction][0], col + directions[direction][1]
            row, col = nextRow, nextCol
        return matrix
