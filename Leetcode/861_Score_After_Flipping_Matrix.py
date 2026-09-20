class Solution:
    def matrixScore(self, grid):
        R,C=len(grid),len(grid[0])
        for r in range(R):
            if grid[r][0]==0:
                for c in range(C): grid[r][c]^=1
        for c in range(1,C):
            if sum(grid[r][c] for r in range(R))*2<R:
                for r in range(R): grid[r][c]^=1
        return sum(int(''.join(map(str,row)),2) for row in grid)