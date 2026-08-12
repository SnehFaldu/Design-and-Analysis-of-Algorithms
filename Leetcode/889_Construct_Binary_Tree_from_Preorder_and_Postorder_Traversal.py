from typing import List, Optional
class Solution:
    def constructFromPrePost(
        self,
        preorder: List[int],
        postorder: List[int]
    ) -> Optional['TreeNode']:

        post_index = {value: i for i, value in enumerate(postorder)}

        def build(pre_l, pre_r, post_l, post_r):
            if pre_l > pre_r:
                return None

            root = TreeNode(preorder[pre_l])

            if pre_l == pre_r:
                return root

            left_root = preorder[pre_l + 1]
            left_end = post_index[left_root]
            left_size = left_end - post_l + 1

            root.left = build(
                pre_l + 1,
                pre_l + left_size,
                post_l,
                left_end
            )

            root.right = build(
                pre_l + left_size + 1,
                pre_r,
                left_end + 1,
                post_r - 1
            )

            return root

        return build(
            0,
            len(preorder) - 1,
            0,
            len(postorder) - 1
        )
