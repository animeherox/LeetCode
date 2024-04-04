class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0
        for char in s:
            if char == "(":
                depth += 1
                maxDepth = max(depth, maxDepth)
            elif char == ")":
                depth -= 1
        return maxDepth
