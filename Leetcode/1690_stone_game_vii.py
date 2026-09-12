class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)
        prefix = [0] * (n + 1)
        for i, x in enumerate(stones):
            prefix[i + 1] = prefix[i] + x

        dp = [0] * n
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                total = prefix[r + 1] - prefix[l]
                left = total - stones[l] - dp[l + 1]
                right = total - stones[r] - dp[l]
                dp[l] = max(left, right)
        return dp[0]
