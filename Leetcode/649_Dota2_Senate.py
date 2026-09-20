class Solution:
    def predictPartyVictory(self, senate):
        n=len(senate); r=deque(); d=deque()
        for i,c in enumerate(senate): (r if c=='R' else d).append(i)
        while r and d:
            a,b=r.popleft(),d.popleft()
            if a<b: r.append(a+n)
            else: d.append(b+n)
        return 'Radiant' if r else 'Dire'