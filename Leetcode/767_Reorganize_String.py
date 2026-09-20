class Solution:
    def reorganizeString(self, s):
        f=Counter(s)
        if max(f.values())>(len(s)+1)//2: return ''
        h=[(-v,c) for c,v in f.items()]; heapq.heapify(h); ans=[]; prev=(0,'')
        while h:
            cnt,c=heapq.heappop(h); ans.append(c); cnt+=1
            if prev[0]<0: heapq.heappush(h,prev)
            prev=(cnt,c)
        return ''.join(ans)