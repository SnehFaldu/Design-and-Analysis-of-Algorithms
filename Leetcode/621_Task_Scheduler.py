class Solution:
    def leastInterval(self, tasks, n):
        f=Counter(tasks); mx=max(f.values()); cnt=sum(x==mx for x in f.values())
        return max(len(tasks),(mx-1)*(n+1)+cnt)