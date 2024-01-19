class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def generateTree(x, y, size):
            value = grid[x][y]
            isLeaf = True
            root = Node(True if value==1 else False, False, None, None, None, None)
            for i in range(size):
                for j in range(size):
                    if grid[x+i][y+j] != value:
                        isLeaf = False
                        break
            if isLeaf:
                root.isLeaf = True
            else:
                halfSize = size//2
                root.topLeft = generateTree(x, y, halfSize)
                root.topRight = generateTree(x, y+halfSize, halfSize)
                root.bottomLeft = generateTree(x+halfSize, y, halfSize)
                root.bottomRight = generateTree(x+halfSize, y+halfSize, halfSize)
            return root
        return generateTree(0, 0, len(grid))