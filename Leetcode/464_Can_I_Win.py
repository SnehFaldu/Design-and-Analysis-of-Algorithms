from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total < desiredTotal:
            return False

        @lru_cache(None)
        def win(used: int, remaining: int) -> bool:
            for pick in range(1, maxChoosableInteger + 1):
                bit = 1 << (pick - 1)
                if used & bit:
                    continue
                if pick >= remaining or not win(used | bit, remaining - pick):
                    return True
            return False

        return win(0, desiredTotal)
