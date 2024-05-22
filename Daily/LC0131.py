from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(start: int):
            if start == length:
                result.append(currentPartition[:])
                return
            for end in range(start, length):
                if palindromeFlags[start][end]:
                    currentPartition.append(s[start:end+1])
                    dfs(end+1)
                    currentPartition.pop()
        length = len(s)
        palindromeFlags = [[True]*length for _ in range(length)]
        for i in range(length-1, -1, -1):
            for j in range(i+1, length):
                palindromeFlags[i][j] = s[i] == s[j] and palindromeFlags[i+1][j-1]
        result = []
        currentPartition = []
        dfs(0)
        return result
