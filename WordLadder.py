from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def extend_ladder(current_mappings, opposite_mappings, queue):
            for _ in range(len(queue)):
                word = queue.popleft()
                word_step_count = current_mappings[word]
                word_list = list(word)
                for i in range(len(word_list)):
                    temp = word_list[i]
                    for j in range(26):
                        word_list[i] = chr(ord('a') + j)
                        new_word = ''.join(word_list)
                        if new_word in current_mappings or new_word not in words:
                            continue
                        if new_word in opposite_mappings:
                            return word_step_count + 1 + opposite_mappings[new_word]
                        current_mappings[new_word] = word_step_count + 1
                        queue.append(new_word)
                    word_list[i] = temp
            return -1
        words = set(wordList)
        if endWord not in words:
            return 0
        # Try BFS from both sides
        begin_queue = deque([beginWord])
        end_queue = deque([endWord])
        begin_mappings = {beginWord: 0}
        end_mappings = {endWord: 0}
        while begin_queue and end_queue:
            # Try minimize expansion of search space
            if len(begin_queue) <= len(end_queue):
                result = extend_ladder(begin_mappings, end_mappings, begin_queue)
            else:
                result = extend_ladder(end_mappings, begin_mappings, end_queue)
            # If a connection is found, return the total number of steps
            if result != -1:
                return result + 1
        return 0
