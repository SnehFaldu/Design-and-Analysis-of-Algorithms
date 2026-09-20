class Solution:
    def minDeletionSize(self, strs):
        n=len(strs); fixed=[False]*(n-1); ans=0
        for col in range(len(strs[0])):
            if any(not fixed[i] and strs[i][col]>strs[i+1][col] for i in range(n-1)):
                ans+=1; continue
            for i in range(n-1):
                if strs[i][col]<strs[i+1][col]: fixed[i]=True
        return ans