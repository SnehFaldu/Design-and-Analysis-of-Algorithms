class Solution:
    def findUnsortedSubarray(self, nums):
        n=len(nums); l=0
        while l<n-1 and nums[l]<=nums[l+1]: l+=1
        if l==n-1: return 0
        r=n-1
        while r>0 and nums[r-1]<=nums[r]: r-=1
        lo,hi=min(nums[l:r+1]),max(nums[l:r+1])
        while l>0 and nums[l-1]>lo: l-=1
        while r<n-1 and nums[r+1]<hi: r+=1
        return r-l+1