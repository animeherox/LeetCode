class Solution:
    def decodeString(self, s: str) -> str:
        def stringToInt(s):
            ans = 0
            for ch in s:
                ans *= 10
                ans += int(ch) - int("0")
            return ans
        
        def decode(s):
            ans = ""
            prev = repetitions = depth = 0
            for i in range(len(s)):
                if (depth == 0 and "a" <= s[i] and s[i] <= "z"):
                    ans += s[i]
                    prev = i + 1
                elif s[i] == "[":
                    depth += 1
                    if depth == 1:
                        repetitions = stringToInt(s[prev:i])
                        prev = i + 1
                elif s[i] == "]":
                    depth -= 1
                    if depth == 0:
                        segment = decode(s[prev:i])
                        ans += segment * repetitions
                        repetitions = 0
                        prev = i + 1
            return ans
        
        return decode(s)
