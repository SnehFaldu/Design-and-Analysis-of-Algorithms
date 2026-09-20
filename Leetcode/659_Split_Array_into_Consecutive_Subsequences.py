class Solution:
    def isPossible(self, nums):
        count=Counter(nums); tails=defaultdict(int)
        for x in nums:
            if count[x]==0: continue
            count[x]-=1
            if tails[x-1]: tails[x-1]-=1; tails[x]+=1
            elif count[x+1] and count[x+2]:
                count[x+1]-=1; count[x+2]-=1; tails[x+2]+=1
            else: return False
        return True