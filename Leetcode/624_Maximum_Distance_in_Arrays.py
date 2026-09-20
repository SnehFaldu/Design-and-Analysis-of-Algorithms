class Solution:
    def maxDistance(self, arrays):
        mn,mx=arrays[0][0],arrays[0][-1]; ans=0
        for a in arrays[1:]:
            ans=max(ans,a[-1]-mn,mx-a[0]); mn=min(mn,a[0]); mx=max(mx,a[-1])
        return ans