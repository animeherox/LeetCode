from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        def canMake(day: int) -> bool:
            bouquets = 0
            consecutive = 0
            for bloom in bloomDay:
                if bloom <= day:
                    consecutive += 1
                    if consecutive == k:
                        consecutive = 0
                        bouquets += 1
                else:
                    consecutive = 0
            return bouquets >= m
        
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMake(mid):
                right = mid
            else:
                left = mid + 1
        return left
