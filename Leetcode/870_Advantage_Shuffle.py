class Solution:
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        n = len(nums2)
        ans = [0] * n
        indices = sorted(range(n), key=lambda i: nums2[i], reverse=True)
        l = 0
        r = n - 1
        for i in indices:
            if nums1[r] > nums2[i]:
                ans[i] = nums1[r]
                r -= 1
            else:
                ans[i] = nums1[l]
                l += 1
        return ans