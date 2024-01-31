class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            index = ord(letter) - ord('a') # Map letter to child index
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_word = True     

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index, len(word)):
                char = word[i]
                char_index = ord(char) - ord('a')
                if char == '.':
                    return any(child is not None and dfs(i + 1, child) for child in node.children)
                elif node.children[char_index] is None:
                    return False
                else:
                    node = node.children[char_index]
            return node.is_word
        return dfs(0, self.root)
