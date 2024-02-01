class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0 # Pointers for ends of sliding window
        best = 0
        lenS = len(s) # Avoid repeated queries
        seen = set()
        while (j < lenS):
            if s[j] not in seen:
                best = max(best, j-i+1)
            else:
                while s[j] in seen: # Shrink from left until s[j] can be added
                    seen.remove(s[i])
                    i += 1
            seen.add(s[j]) # Keep incrementing right end of window
            j += 1
        return best