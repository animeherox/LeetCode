class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0)}
        x = y = 0
        vectors = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1, 0)}
        for direction in path:
            dx, dy = vectors[direction]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False
