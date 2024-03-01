class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        numOnes = s.count("1")
        if numOnes == 0:
            return ""
        return "1"*(numOnes-1) + "0"*(len(s)-numOnes) + "1"
