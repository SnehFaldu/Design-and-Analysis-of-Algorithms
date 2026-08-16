class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        ans = []

        for k, trim in queries:
            arr = []

            for i, num in enumerate(nums):
                value = num[-trim:]
                arr.append((value, i))

            arr.sort()

            ans.append(arr[k - 1][1])

        return ans
