class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        rows=list(map(max,grid)); cols=[max(row[c] for row in grid) for c in range(len(grid[0]))]
        return sum(min(rows[r],cols[c])-grid[r][c] for r in range(len(grid)) for c in range(len(grid[0])))