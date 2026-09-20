class Solution:
    def movesToMakeZigzag(self, nums):
        n = len(nums)
        def calculate(start):
            moves = 0
            for i in range(start, n, 2):
                left = nums[i - 1] if i > 0 else float('inf')
                right = nums[i + 1] if i + 1 < n else float('inf')
                target = min(left, right) - 1
                if nums[i] > target:
                    moves += nums[i] - target
            return moves
        return min(calculate(0), calculate(1))