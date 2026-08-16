class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        answer = 0

        for left in range(n):
            count = 0
            for right in range(left, n):
                if nums[right] == target:
                    count += 1

                length = right - left + 1
                if 2 * count > length:
                    answer += 1

        return answer
