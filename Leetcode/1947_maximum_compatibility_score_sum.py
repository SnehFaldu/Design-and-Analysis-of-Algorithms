class Solution:
    def maxCompatibilitySum(self, students, mentors):
        m = len(students)
        score = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                score[i][j] = sum(a == b for a, b in zip(students[i], mentors[j]))

        dp = [-1] * (1 << m)
        dp[0] = 0

        for mask in range(1 << m):
            i = mask.bit_count()
            if i == m:
                continue
            for j in range(m):
                if not (mask >> j) & 1:
                    nxt = mask | (1 << j)
                    dp[nxt] = max(dp[nxt], dp[mask] + score[i][j])

        return dp[-1]
