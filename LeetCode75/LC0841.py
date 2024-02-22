from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        numVisited = 0
        numRooms = len(rooms)
        visited = {0}
        keyStack = [0]
        while keyStack:
            room = keyStack.pop()
            numVisited += 1
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    keyStack.append(key)
        return numVisited == numRooms
