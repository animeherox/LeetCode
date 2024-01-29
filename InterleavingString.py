class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 + len_s2 != len(s3):
            return False
        dp = [True] + [False]*len_s2
        for i in range(len_s1+1):
            for j in range(len_s2+1):
                k = i+j-1
                if i:
                    dp[j] &= s1[i - 1] == s3[k]
                if j:
                    dp[j] |= dp[j - 1] and s2[j - 1] == s3[k]
        return dp[-1]
