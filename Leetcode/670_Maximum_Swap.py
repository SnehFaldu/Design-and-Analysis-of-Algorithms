class Solution:
    def maximumSwap(self, num):
        a=list(str(num)); last={int(c):i for i,c in enumerate(a)}
        for i,c in enumerate(a):
            for d in range(9,int(c),-1):
                if last.get(d,-1)>i:
                    j=last[d]; a[i],a[j]=a[j],a[i]; return int(''.join(a))
        return num