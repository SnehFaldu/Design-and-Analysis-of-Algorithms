# LeetCode provides TreeNode.
class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            left_skip, left_take = dfs(node.left)
            right_skip, right_take = dfs(node.right)
            skip = max(left_skip, left_take) + max(right_skip, right_take)
            take = node.val + left_skip + right_skip
            return skip, take

        return max(dfs(root))
