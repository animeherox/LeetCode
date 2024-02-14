from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        index, num_words = 0, len(words)
        while index < num_words:
            line = []
            count = len(words[index])
            line.append(words[index])
            index += 1
            while index < num_words and count + 1 + len(words[index]) <= maxWidth:
                count += 1 + len(words[index])
                line.append(words[index])
                index += 1
            # Check if we're on the last line
            if index == num_words or len(line) == 1:
                justified_line = ' '.join(line)
                right_padding = ' ' * (maxWidth - len(justified_line))
                result.append(justified_line + right_padding)
                continue
            line_spaces = maxWidth - (count - len(line) + 1)
            space_width, extra_spaces = divmod(line_spaces, len(line)-1)
            spaced_line = []
            for i, word in enumerate(line[:-1]):
                spaced_line.append(word)
                spaced_line.append(' ' * (space_width + (1 if i < extra_spaces else 0)))
            spaced_line.append(line[-1])
            result.append(''.join(spaced_line))
        return result
