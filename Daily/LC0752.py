from collections import deque
from typing import List, Tuple

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def stringToState(state: str) -> List[int]:
            return [int(c) for c in state]
        
        def genNextStates(state: Tuple[int]):
            nextStates = []
            originalState = state
            state = list(state)
            for i in range(4):
                originalDigit = originalState[i]
                state[i] = 9 if originalDigit == 0 else originalDigit - 1
                nextStates.append(tuple(state))
                state[i] = 0 if originalDigit == 9 else originalDigit + 1
                nextStates.append(tuple(state))
                state[i] = originalDigit
            return nextStates
        
        def extend(startFrontier, endFrontier, queue):
            for _ in range(len(queue)):
                currentState = queue.popleft()
                currentStep = startFrontier[tuple(currentState)]
                for nextState in genNextStates(currentState):
                    if nextState in deadendSet or nextState in startFrontier:
                        continue
                    if nextState in endFrontier:
                        return currentStep + 1 + endFrontier[nextState]
                    startFrontier[nextState] = currentStep + 1
                    queue.append(nextState)
            return -1
        
        def bidirectionalBfs():
            startFrontier = {(0,0,0,0): 0}
            targetState = stringToState(target)
            endFrontier = {tuple(targetState): 0}
            startQueue = deque([[0,0,0,0]])
            endQueue = deque([targetState])
            while startQueue and endQueue:
                result = extend(startFrontier, endFrontier, startQueue) if len(startQueue) <= len(endQueue) else extend(endFrontier, startFrontier, endQueue)
                if result != -1:
                    return result
            return -1
        
        if target == '0000':
            return 0
        deadendSet = set([tuple(stringToState(deadend)) for deadend in deadends])
        if (0,0,0,0) in deadendSet:
            return -1
        return bidirectionalBfs()