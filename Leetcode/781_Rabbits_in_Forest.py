class Solution:
    def numRabbits(self, answers):
        c=Counter(answers); ans=0
        for x,v in c.items(): ans += ((v+x)//(x+1))*(x+1)
        return ans