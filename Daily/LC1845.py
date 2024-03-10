from heapq import heappush, heappop

class SeatManager:

    def __init__(self, n: int):
        self.available = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available, seatNumber)
