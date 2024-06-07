from typing import List

class Trie:
    def __init__(self):
        # Initialize a Trie node with children for each letter of the alphabet and a flag to mark the end of a word
        self.children = [None] * 26
        self.ref = -1

    def insert(self, word, idx):
        # Insert a word into the Trie. Iterate through each character in the word, calculate its index, and create new Trie nodes as necessary.
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.ref = idx

    def search(self, word):
        # Search for a word in the Trie. Traverse the Trie based on each character in the word. If we reach the end and the is_end_of_word flag is True, the word exists in the trie.
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return -1
            node = node.children[index]
            if node.ref != -1:
                return node.ref
        return -1

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for idx, word in enumerate(dictionary):
            trie.insert(word, idx)
        answer = []
        for word in sentence.split():
            index = trie.search(word)
            answer.append(dictionary[index] if index != -1 else word)
        return " ".join(answer)
