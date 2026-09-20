class Solution:
    def minAddToMakeValid(self, s):
        bal=add=0
        for c in s:
            if c=='(': bal+=1
            elif bal: bal-=1
            else: add+=1
        return add+bal