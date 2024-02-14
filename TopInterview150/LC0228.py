from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) == 0:
            return ranges
        start = nums[0]
        end = nums[0]
        for n in nums[1:]:
            if n == end+1:
                end += 1
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start)+"->"+str(end))
                start = end = n
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start)+"->"+str(end))
        return ranges