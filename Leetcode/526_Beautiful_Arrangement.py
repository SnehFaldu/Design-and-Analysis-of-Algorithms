from functools import lru_cache

class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def dp(mask: int) -> int:
            position = mask.bit_count() + 1
            if position > n:
                return 1
            total = 0
            for value in range(1, n + 1):
                bit = 1 << (value - 1)
                if mask & bit == 0 and (
                    value % position == 0 or position % value == 0
                ):
                    total += dp(mask | bit)
            return total

        return dp(0)
