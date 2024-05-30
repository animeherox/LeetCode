from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        tripletCount = 0
        for i in range(n-1):
            for j in range(i+1, n):
                for k in range(j, n):
                    a, b = prefix[j] ^ prefix[i], prefix[k+1] ^ prefix[j]
                    if a == b:
                        tripletCount += 1
        return tripletCount
