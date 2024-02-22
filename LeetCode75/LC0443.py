from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write, length = 0, 0, len(chars)
        while read < length:
            next_read = read+1
            while next_read < length and chars[next_read] == chars[read]:
                next_read += 1
            chars[write] = chars[read]
            write += 1
            if next_read - read > 1:
                count = str(next_read-read)
                for digit in count:
                    chars[write] = digit
                    write += 1
            read = next_read
        return write
