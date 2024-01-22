class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        def dfs(openCount, closeCount, path):
            if openCount > n or closeCount > n or closeCount > openCount:
                return
            elif closeCount == n:
                combinations.append(path)
                return
            dfs(openCount+1, closeCount, path+'(')
            dfs(openCount, closeCount+1, path+')')
        dfs(1, 0, '(')
        return combinations