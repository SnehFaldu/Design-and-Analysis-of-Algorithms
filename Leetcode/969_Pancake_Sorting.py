class Solution:
    def pancakeSort(self, arr):
        ans=[]
        for size in range(len(arr),1,-1):
            i=arr.index(size)
            if i==size-1: continue
            if i:
                ans.append(i+1); arr[:i+1]=reversed(arr[:i+1])
            ans.append(size); arr[:size]=reversed(arr[:size])
        return ans