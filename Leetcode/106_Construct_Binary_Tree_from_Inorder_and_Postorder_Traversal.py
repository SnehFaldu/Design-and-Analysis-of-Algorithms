from typing import List, Optional
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional['TreeNode']:
        index = {value: i for i, value in enumerate(inorder)}
        def build(in_l, in_r, post_l, post_r):
            if in_l > in_r:
                return None
            root_value = postorder[post_r]
            root = TreeNode(root_value)
            mid = index[root_value]
            left_size = mid - in_l
            root.left = build(
                in_l,
                mid - 1,
                post_l,
                post_l + left_size - 1
            )
            root.right = build(
                mid + 1,
                in_r,
                post_l + left_size,
                post_r - 1
            )
            return root
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
