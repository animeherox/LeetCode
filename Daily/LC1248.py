from collections import Counter
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCount = Counter({0: 1})
        ans = tempOddCount = 0
        for n in nums:
            tempOddCount += n & 1
            ans += oddCount[tempOddCount - k]
            oddCount[tempOddCount] += 1
        return ans
