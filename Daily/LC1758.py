class Solution:
    def minOperations(self, s: str) -> int:
        mismatch_count = sum(char != '01'[i%2] for i, char in enumerate(s))
        return min(mismatch_count, len(s) - mismatch_count)
