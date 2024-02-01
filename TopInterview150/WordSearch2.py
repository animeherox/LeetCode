class Trie:
    def __init__(self):
        self.children: List[Trie | None] = [None] * 26
        self.ref: int = -1

    def insert(self, word: str, ref: int):
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.ref = ref

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_found = []
        m, n = len(board), len(board[0])
        # Define DFS for all possible words from a point with a Trie dictionary
        def dfs(node: Trie, i: int, j: int):
            trie_index = ord(board[i][j]) - ord('a')
            if node.children[trie_index] is None:
                return
            node = node.children[trie_index]
            # If we've completed a word, record it and mark as found in Trie
            if node.ref >= 0:
                words_found.append(words[node.ref])
                node.ref = -1
            # Temporarily mark board spot as visited
            temp = board[i][j]
            board[i][j] = '.'
            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and board[x][y] != ".":
                    dfs(node, x, y)
            # Unmark spot after DFS finishes
            board[i][j] = temp
        
        word_trie = Trie()
        for index, word in enumerate(words):
            word_trie.insert(word, index)
        for i in range(m):
            for j in range(n):
                dfs(word_trie, i, j)
        return words_found
