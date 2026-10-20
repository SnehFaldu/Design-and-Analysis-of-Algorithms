from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        sides = [0] * 4

        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return True
            seen = set()
            for side in range(4):
                if sides[side] in seen or sides[side] + matchsticks[index] > target:
                    continue
                seen.add(sides[side])
                sides[side] += matchsticks[index]
                if backtrack(index + 1):
                    return True
                sides[side] -= matchsticks[index]
                if sides[side] == 0:
                    break
            return False

        return backtrack(0)
