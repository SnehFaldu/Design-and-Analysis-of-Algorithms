from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()

        small = nums[:(n + 1) // 2][::-1]
        large = nums[(n + 1) // 2:][::-1]

        result = []

        for i in range(len(small)):
            result.append(small[i])
            if i < len(large):
                result.append(large[i])

        nums[:] = result
