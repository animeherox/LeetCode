class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = [[i] for i in range(1,n+1)]
        for _ in range(k-1):
            newOutput = []
            for partial in output:
                for i in range(partial[-1]+1, n+1):
                    newOutput.append(partial+[i])
            output = newOutput
        return output