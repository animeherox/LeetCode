class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNumber(x: int):
            square_total = 0
            while x:
                x, digit = divmod(x, 10)
                square_total += digit*digit
            return square_total
        
        # Use slow and fast pointer to detect cycles
        slow = n
        fast = nextNumber(slow)

        while slow != fast:
            slow = nextNumber(slow)
            fast = nextNumber(nextNumber(fast))
        
        return slow == 1