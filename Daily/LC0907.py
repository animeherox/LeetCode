from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] >= val:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        base = 10**9 + 7
        result = sum((i - left[i])*(right[i] - i)*val for i, val in enumerate(arr)) % base
        return result
