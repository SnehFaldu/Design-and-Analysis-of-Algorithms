class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)
        rem1 = sorted(x for x in nums if x % 3 == 1)
        rem2 = sorted(x for x in nums if x % 3 == 2)
        remainder = total % 3
        if remainder == 0:
            return total
        remove = []
        if remainder == 1:
            if rem1:
                remove.append(rem1[0])
            if len(rem2) >= 2:
                remove.append(rem2[0] + rem2[1])
        else:
            if rem2:
                remove.append(rem2[0])
            if len(rem1) >= 2:
                remove.append(rem1[0] + rem1[1])
        if not remove:
            return 0
        return total - min(remove)