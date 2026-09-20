class Solution:
    def monotoneIncreasingDigits(self, n):
        a=list(str(n)); marker=len(a)
        for i in range(len(a)-1,0,-1):
            if a[i]<a[i-1]:
                a[i-1]=str(int(a[i-1])-1); marker=i
        for i in range(marker,len(a)): a[i]='9'
        return int(''.join(a))