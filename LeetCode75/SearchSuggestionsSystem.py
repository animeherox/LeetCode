from typing import List, Optional

class Trie:
    def __init__(self):
        self.children: List[Optional[Trie]] = [None]*26
        self.indices: List[int] = []

    def insert(self, word: str, index: int) -> None:
        node = self
        for letter in word:
            char_index = ord(letter) - ord('a') # Map letter to child index
            if node.children[char_index] is None:
                node.children[char_index] = Trie()
            node = node.children[char_index]
            if len(node.indices) < 3:
                node.indices.append(index)

    def search(self, word: str) -> bool:
        node = self
        results = [[] for _ in range(len(word))]
        for i, letter in enumerate(word):
            char_index = ord(letter) - ord('a')
            if node.children[char_index] is None:
                break
            node = node.children[char_index]
            results[i] = node.indices
        return results

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        productTrie = Trie()
        for i, product in enumerate(products):
            productTrie.insert(product, i)
        indicesList = productTrie.search(searchWord)
        return [[products[index] for index in sublist] for sublist in indicesList]
