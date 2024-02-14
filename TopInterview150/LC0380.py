import random

class RandomizedSet:

    def __init__(self):
        # Create a list for random choices, and a dict for indices
        self.indexDict = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.indexDict:
            return False
        self.indexDict[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexDict:
            return False
        # Replace target value with last value, and pop
        index = self.indexDict[val]
        lastVal = self.values[-1]
        self.values[index] = lastVal
        self.indexDict[lastVal] = index
        del self.indexDict[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)