class Solution:
    def reconstructMatrix(self, upper, lower, colsum):
        n = len(colsum)
        if sum(colsum) != upper + lower:
            return []
        matrix = [[0] * n for _ in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                matrix[0][i] = 1
                matrix[1][i] = 1
                upper -= 1
                lower -= 1
        if upper < 0 or lower < 0:
            return []
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    matrix[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    matrix[1][i] = 1
                    lower -= 1
                else:
                    return []
        if upper != 0 or lower != 0:
            return []
        return matrix