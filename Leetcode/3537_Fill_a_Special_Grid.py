class Solution:
    def specialGrid(self, n):
        size = 2 ** n
        grid = [[0] * size for _ in range(size)]

        def fill(r, c, length, start):
            if length == 1:
                grid[r][c] = start
                return

            half = length // 2
            block = half * half
            fill(r, c + half, half, start)
            fill(r + half, c + half, half, start + block)
            fill(r + half, c, half, start + 2 * block)
            fill(r, c, half, start + 3 * block)

        fill(0, 0, size, 0)
        return grid
