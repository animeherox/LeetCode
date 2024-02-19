from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        # Create the root using the last value of the post-order traverse
        rootVal = postorder[-1]
        root = TreeNode(rootVal)

        # Split the two lists based on the root
        index = inorder.index(rootVal)

        # Fill in subtrees recursively
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])

        return root
