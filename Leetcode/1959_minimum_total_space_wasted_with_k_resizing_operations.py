class Solution:
    def minSpaceWastedKResizing(self, nums, k):
        n = len(nums)
        INF = 10**18
        prefix = [0] * (n + 1)

        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x

        # dp[segments][i] = minimum waste for first i elements.
        dp = [[INF] * (n + 1) for _ in range(k + 2)]
        dp[0][0] = 0

        for segments in range(1, k + 2):
            for i in range(1, n + 1):
                mx = 0
                for j in range(i, 0, -1):
                    mx = max(mx, nums[j - 1])
                    waste = mx * (i - j + 1) - (prefix[i] - prefix[j - 1])
                    dp[segments][i] = min(
                        dp[segments][i],
                        dp[segments - 1][j - 1] + waste
                    )

        return dp[k + 1][n]
