from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        ans = []
        for v in target:
            i += 1
            while i < v:
                i += 1
                ans.extend(['Push', 'Pop'])
            ans.append('Push')
        return ans
