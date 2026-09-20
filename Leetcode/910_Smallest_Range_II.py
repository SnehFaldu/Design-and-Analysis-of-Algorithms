class Solution:
    def smallestRangeII(self, nums, k):
        nums.sort(); ans=nums[-1]-nums[0]
        for i in range(len(nums)-1):
            hi=max(nums[i]+k,nums[-1]-k); lo=min(nums[0]+k,nums[i+1]-k)
            ans=min(ans,hi-lo)
        return ans