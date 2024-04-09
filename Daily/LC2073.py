from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i, ticketCount in enumerate(tickets):
            if i <= k:
                ans += min(tickets[k], ticketCount)
            else:
                ans += min(tickets[k]-1, ticketCount)
        return ans
