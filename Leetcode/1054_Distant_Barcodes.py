class Solution:
    def rearrangeBarcodes(self, barcodes):
        c=Counter(barcodes); h=[(-v,x) for x,v in c.items()]; heapq.heapify(h)
        ans=[]; prev=(0,None)
        while h:
            cnt,x=heapq.heappop(h); ans.append(x); cnt+=1
            if prev[0]<0: heapq.heappush(h,prev)
            prev=(cnt,x)
        return ans