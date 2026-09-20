class Solution:
    def smallestSubsequence(self, s):
        last={c:i for i,c in enumerate(s)}; st=[]; seen=set()
        for i,c in enumerate(s):
            if c in seen: continue
            while st and c<st[-1] and last[st[-1]]>i:
                seen.remove(st.pop())
            st.append(c); seen.add(c)
        return ''.join(st)