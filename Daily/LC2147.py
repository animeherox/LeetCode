class Solution:
    def numberOfWays(self, corridor: str) -> int:
        base = 10**9 + 7
        ans, prevSeat, numSeats = 1, -1, 0
        for i, c in enumerate(corridor):
            if c == 'S':
                numSeats += 1
                if numSeats > 2 and numSeats & 1:
                    ans = ans * (i - prevSeat) % base
                prevSeat = i
        return ans if numSeats > 1 and numSeats % 2 == 0 else 0
