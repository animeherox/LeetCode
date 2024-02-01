import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('','',string.punctuation)).replace(' ','').lower()
        print(s)
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True