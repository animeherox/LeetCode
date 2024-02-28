from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        smoothed = [[0]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                pixel_sum = pixel_count = 0
                for i in range(max(0, row-1), min(m, row+2)):
                    for j in range(max(0, col-1), min(n, col+2)):
                        pixel_count += 1
                        pixel_sum += img[i][j]
                smoothed[row][col] = pixel_sum // pixel_count
        return smoothed
