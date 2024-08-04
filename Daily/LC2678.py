from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(detail[11:13] > "60" for detail in details)
