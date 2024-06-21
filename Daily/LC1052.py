from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        unsatisfied = sum(customer * grumpiness for customer, grumpiness in zip(customers, grumpy))
        n = sum(customers)
        tempImproved = maxImproved = 0
        for i, (customer, grumpiness) in enumerate(zip(customers, grumpy), 1):
            tempImproved += customer * grumpiness
            if (j := i - minutes) >= 0:
                maxImproved = max(maxImproved, n - (unsatisfied - tempImproved))
                tempImproved -= customers[j] * grumpy[j]
        return maxImproved
