class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        answer = 0
        for left in range(n):
            seen = set()
            even = 0
            odd = 0

            for right in range(left, n):
                x = nums[right]
                if x not in seen:
                    seen.add(x)
                    if x % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                if even == odd:
                    answer = max(answer, right - left + 1)
        return answer
