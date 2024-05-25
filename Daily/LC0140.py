from typing import List

class Trie:
    def __init__(self):
        # Initialize a Trie node with children for each letter of the alphabet and a flag to mark the end of a word
        self.children = [None] * 26
        self.is_end_of_word = False

    def insert(self, word):
        # Insert a word into the Trie. Iterate through each character in the word, calculate its index, and create new Trie nodes as necessary.
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end_of_word = True

    def search(self, word):
        # Search for a word in the Trie. Traverse the Trie based on each character in the word. If we reach the end and the is_end_of_word flag is True, the word exists in the trie.
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.is_end_of_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(substring):
            # Depth-First Search function to build all possible sentences
            if not substring:
                # If there are no more characters left, we return an empty list within a list to signify a completed sentence.
                return [[]]
            results = []
            # Check every possible prefix of the substring, if it is in the Trie (meaning it's a valid word), we recursively call dfs on the remaining substring.
            for i in range(1, len(substring) + 1):
                if trie.search(substring[:i]):
                    for extension in dfs(substring[i:]):
                        results.append([substring[:i]] + extension)
            return results
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        partialSentences = dfs(s)
        fullSentences = [' '.join(words) for words in partialSentences]
        return fullSentences
