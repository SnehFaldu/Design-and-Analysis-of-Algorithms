class Solution:
    def lengthOfLIS(self, nums):
        tails = []
        for x in nums:
            l, r = 0, len(tails)
            while l < r:
                m = (l + r) // 2
                if tails[m] < x:
                    l = m + 1
                else:
                    r = m
            if l == len(tails):
                tails.append(x)
            else:
                tails[l] = x
        return len(tails)
