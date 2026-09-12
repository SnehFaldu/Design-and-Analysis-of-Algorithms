class Solution:
    def minFlips(self, s):
        n = len(s)
        s += s
        mismatch0 = mismatch1 = 0
        ans = n

        for i, c in enumerate(s):
            e0 = '0' if i % 2 == 0 else '1'
            e1 = '1' if i % 2 == 0 else '0'
            mismatch0 += c != e0
            mismatch1 += c != e1

            if i >= n:
                old = s[i - n]
                oe0 = '0' if (i - n) % 2 == 0 else '1'
                oe1 = '1' if (i - n) % 2 == 0 else '0'
                mismatch0 -= old != oe0
                mismatch1 -= old != oe1

            if i >= n - 1:
                ans = min(ans, mismatch0, mismatch1)

        return ans
