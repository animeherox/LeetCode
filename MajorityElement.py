class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count: int = 0 # Keeps count of candidate majority number
        for n in nums:
            if count == 0:
                ans = n # Set new candidate majority number
            count += (1 if n==ans else -1)
        return ans
