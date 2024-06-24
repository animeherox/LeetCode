from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        length = len(nums)
        flips = [0] * (length + 1)
        totalFlips = 0
        flipCounter = 0
        for i, num in enumerate(nums):
            flipCounter += flips[i]
            if (num + flipCounter) % 2 == 0:
                if i + k > length:
                    return -1
                flips[i] += 1
                flips[i+k] -= 1
                flipCounter += 1
                totalFlips += 1
        return totalFlips
