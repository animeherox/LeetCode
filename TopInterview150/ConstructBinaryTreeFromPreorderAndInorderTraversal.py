class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildSubtree(preorderIndex, inorderIndex, treeSize):
            if treeSize <= 0:
                return None
            root_val = preorder[preorderIndex]
            inorder_root_index = index_mapping[root_val]
            left_subtree = buildSubtree(
                preorderIndex + 1,
                inorderIndex,
                inorder_root_index - inorderIndex)
            right_subtree = buildSubtree(
                preorderIndex + 1 + inorder_root_index - inorderIndex,
                inorder_root_index + 1,
                treeSize - inorder_root_index + inorderIndex - 1)
            return TreeNode(root_val, left_subtree, right_subtree)
        index_mapping = {value: i for i, value in enumerate(inorder)}
        return buildSubtree(0, 0, len(preorder))
