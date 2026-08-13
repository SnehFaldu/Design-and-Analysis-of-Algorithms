from typing import List

class Solution:
    def construct(self, grid: List[List[int]]):
        n = len(grid)

        def build(r, c, size):
            first = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(first == 1, True, None, None, None, None)

            half = size // 2

            top_left = build(r, c, half)
            top_right = build(r, c + half, half)
            bottom_left = build(r + half, c, half)
            bottom_right = build(r + half, c + half, half)

            return Node(
                True,
                False,
                top_left,
                top_right,
                bottom_left,
                bottom_right
            )

        return build(0, 0, n)
