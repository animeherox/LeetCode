class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s) # Index of last position in s
        if s_len == 0: # Handle empty string edge case
            return True
        s_ptr = 0 # Current position in s
        for letter in t:
            if letter == s[s_ptr]:
                s_ptr += 1
                if s_ptr >= s_len:
                    return True
        return False