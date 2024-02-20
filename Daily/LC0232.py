class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if not self.outStack:
            self.shiftStacks()
        return self.outStack.pop()

    def peek(self) -> int:
        if not self.outStack:
            self.shiftStacks()
        return self.outStack[-1]

    def empty(self) -> bool:
        return not (self.inStack or self.outStack)
        
    def shiftStacks(self) -> None:
        while self.inStack:
            self.outStack.append(self.inStack.pop())