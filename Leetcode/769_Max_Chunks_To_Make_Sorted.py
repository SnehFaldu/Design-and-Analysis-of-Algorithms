class Solution:
    def maxChunksToSorted(self, arr):
        mx=ans=0
        for i,x in enumerate(arr):
            mx=max(mx,x)
            if mx==i: ans+=1
        return ans