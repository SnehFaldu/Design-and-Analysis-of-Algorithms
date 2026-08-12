from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quickselect: average O(n), in-place.
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = nums[(left + right) // 2]

            i, j = left, right
            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1

                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            if target <= j:
                right = j
            elif target >= i:
                left = i
            else:
                return nums[target]

        return nums[target]
