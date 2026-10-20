from typing import List
from functools import lru_cache

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def score_diff(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            return max(
                nums[left] - score_diff(left + 1, right),
                nums[right] - score_diff(left, right - 1)
            )

        return score_diff(0, len(nums) - 1) >= 0
