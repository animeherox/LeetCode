class SmallestInfiniteSet:

    def __init__(self):
        self.poppedElements = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        self.poppedElements.add(self.smallest)
        output = self.smallest
        while self.smallest in self.poppedElements:
            self.smallest += 1
        return output

    def addBack(self, num: int) -> None:
        if num in self.poppedElements:
            self.poppedElements.remove(num)
            if num < self.smallest:
                self.smallest = num
