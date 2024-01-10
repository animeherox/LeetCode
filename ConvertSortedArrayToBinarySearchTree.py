class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        midpoint = len(nums)//2
        return TreeNode(nums[midpoint], self.sortedArrayToBST(nums[:midpoint]), self.sortedArrayToBST(nums[midpoint+1:]))