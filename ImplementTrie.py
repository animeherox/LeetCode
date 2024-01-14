class Trie:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False

    def insert(self, word: str) -> None:
        node = self
        for letter in word:
            index = ord(letter) - ord('a') # Map letter to child index
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_word = True        

    def search(self, word: str) -> bool:
        node = self
        for letter in word:
            index = ord(letter) - ord('a') # Map letter to child index
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self
        for letter in prefix:
            index = ord(letter) - ord('a') # Map letter to child index
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node is not None