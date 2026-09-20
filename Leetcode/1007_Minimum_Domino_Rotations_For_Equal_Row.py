class Solution:
    def minDominoRotations(self, tops, bottoms):
        def f(x):
            a=b=0
            for t,d in zip(tops,bottoms):
                if t!=x and d!=x: return float('inf')
                a += t!=x; b += d!=x
            return min(a,b)
        x=min(f(tops[0]),f(bottoms[0]))
        return -1 if x==float('inf') else x