class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total, prev_value = 0, 0
        for char in reversed(s):
            if mapping[char] < prev_value:
                total -= mapping[char]
            else:
                total += mapping[char]
            prev_value = mapping[char]
        return total
