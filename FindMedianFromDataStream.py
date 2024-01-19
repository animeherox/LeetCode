from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = [] # Max heap storing the smaller half
        self.large = [] # Min heap storing the larger half

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))
        # Rebalance as needed
        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (self.large[0] - self.small[0]) / 2.0