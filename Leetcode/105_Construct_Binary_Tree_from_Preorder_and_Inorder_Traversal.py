from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional['TreeNode']:
        index = {value: i for i, value in enumerate(inorder)}
        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None
            root_value = preorder[pre_l]
            root = TreeNode(root_value)
            mid = index[root_value]
            left_size = mid - in_l
            root.left = build(
                pre_l + 1,
                pre_l + left_size,
                in_l,
                mid - 1
            )
            root.right = build(
                pre_l + left_size + 1,
                pre_r,
                mid + 1,
                in_r
            )
            return root
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
