class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x:x[1]); end=float('-inf'); ans=0
        for s,e in pairs:
            if s>end: ans+=1; end=e
        return ans