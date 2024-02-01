class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if k >= length:
            numsSet = set(nums)
            return len(numsSet)<length
        else:
            left, right = 0, k+1
            numsSet = set(nums[:k+1])
            if len(numsSet) < k+1:
                return True
            while right < length:
                numsSet.remove(nums[left])
                left += 1
                if nums[right] in numsSet:
                    return True
                else:
                    numsSet.add(nums[right])
                    right += 1
        return False
