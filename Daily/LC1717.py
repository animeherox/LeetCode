class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            return self.maximumGain(s[::-1], y, x)
        ans = 0
        stackAB, stackBA = [], []
        for c in s:
            if c != 'b':
                stackAB.append(c)
            else:
                if stackAB and stackAB[-1] == 'a':
                    stackAB.pop()
                    ans += x
                else:
                    stackAB.append(c)
        while stackAB:
            c = stackAB.pop()
            if c != 'b':
                stackBA.append(c)
            else:
                if stackBA and stackBA[-1] == 'a':
                    stackBA.pop()
                    ans += y
                else:
                    stackBA.append(c)
        return ans
