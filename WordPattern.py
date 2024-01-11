class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordList = set()
        mapping = {}
        words = s.split(" ")
        numWords = len(words)
        if numWords != len(pattern):
            return False
        for i in range(numWords):
            if pattern[i] in mapping and words[i] in wordList:
                if mapping[pattern[i]] != words[i]:
                    return False
            elif pattern[i] in mapping or words[i] in wordList:
                return False
            else:
                mapping[pattern[i]] = words[i]
                wordList.add(words[i])
        return True