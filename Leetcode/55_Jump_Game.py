class Solution:
    def canJump(self, nums):
        farthest = 0
        for i, x in enumerate(nums):
            if i > farthest: return False
            farthest = max(farthest, i+x)
        return True