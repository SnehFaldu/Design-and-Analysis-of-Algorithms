class Solution:
    def countElements(self, nums, k):
        nums.sort()

        n = len(nums)
        if k == 0:
            return n
        threshold = nums[n - k]
        answer = 0
        for x in nums:
            if x < threshold:
                answer += 1

        return answer
