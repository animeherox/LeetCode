from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = Counter(t)
        window_count = Counter()
        num_target_chars, left = 0, 0
        min_left, min_size = -1, float('inf')
        for right, char in enumerate(s):
            window_count[char] += 1
            if target_count[char] >= window_count[char]:
                num_target_chars += 1
            while num_target_chars == len(t):
                # If the current window is smaller, use it
                if right - left + 1 < min_size:
                    min_left = left
                    min_size = right - left + 1
                # Slide left pointer, and update counters
                if target_count[s[left]] == window_count[s[left]]:
                    num_target_chars -= 1
                window_count[s[left]] -= 1
                left += 1
        return "" if min_left < 0 else s[min_left:min_left+min_size]