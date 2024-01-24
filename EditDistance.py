class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1), len(word2)
        dp_table = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]
        for i in range(1, len_word2+1):
            dp_table[0][i] = i
        for i in range(1, len_word1+1):
            dp_table[i][0] = i
            for j in range(1, len_word2+1):
                if word1[i - 1] == word2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                else:
                    dp_table[i][j] = min(
                        dp_table[i-1][j],
                        dp_table[i-1][j-1],
                        dp_table[i][j-1]
                    ) + 1
        return dp_table[len_word1][len_word2]