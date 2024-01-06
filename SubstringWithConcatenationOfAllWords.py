from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordCounts = Counter(words)
        lenS, lenWords, wordSize = len(s), len(words), len(words[0])
        startIndices = []
        for offset in range(wordSize): # Avoid repeats
            i, j = offset, offset
            windowCounts = Counter()
            numMatches = 0

            while j+wordSize <= lenS:
                word = s[j:j+wordSize]
                j += wordSize

                # If the word is not in the list, start window after it
                if word not in wordCounts:
                    i = j
                    windowCounts.clear()
                    numMatches = 0
                    continue

                # Count the new word
                windowCounts[word] += 1
                numMatches += 1

                # If we have excess of the new word, shrink until resolved
                while windowCounts[word] > wordCounts[word]:
                    leftWord = s[i:i+wordSize]
                    i += wordSize
                    windowCounts[leftWord] -= 1
                    numMatches -= 1
                
                if numMatches == lenWords:
                    startIndices.append(i)
        return startIndices
