class Solution:
    def knightDialer(self, n: int) -> int:
        base = 10**9 + 7
        options = [1]*10
        for _ in range(n-1):
            newOptions = [0]*10
            newOptions[0] = options[4] + options[6]
            newOptions[1] = options[6] + options[8]
            newOptions[2] = options[7] + options[9]
            newOptions[3] = options[4] + options[8]
            newOptions[4] = options[0] + options[3] + options[9]
            newOptions[6] = options[0] + options[1] + options[7]
            newOptions[7] = options[2] + options[6]
            newOptions[8] = options[1] + options[3]
            newOptions[9] = options[2] + options[4]
            options = newOptions
        return sum(options) % base
