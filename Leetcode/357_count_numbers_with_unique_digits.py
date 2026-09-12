class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        n = min(n, 10)
        ans = 10
        ways = 9
        available = 9
        for _ in range(2, n + 1):
            ways *= available
            ans += ways
            available -= 1
        return ans
