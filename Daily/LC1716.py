class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, extraDays = divmod(n, 7)
        # Formula for computing deposits over w full weeks: 7 * (7+w) * w/2
        # Formula for computing deposits from d days after w weeks: w*d + (1+d)*d/2
        return int((7 * (7 + weeks) * weeks / 2) + weeks * extraDays + (1 + extraDays) * extraDays / 2)
