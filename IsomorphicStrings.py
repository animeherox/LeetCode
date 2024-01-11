class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length = len(s)
        mappingStoT = {}
        mappingTtoS = {}
        for i in range(length):
            if s[i] in mappingStoT and t[i] in mappingTtoS:
                if mappingStoT[s[i]] != t[i]:
                    return False
            elif s[i] in mappingStoT or t[i] in mappingTtoS:
                return False
            else:
                mappingStoT[s[i]] = t[i]
                mappingTtoS[t[i]] = s[i]
        return True