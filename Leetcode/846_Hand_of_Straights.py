class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand)%groupSize: return False
        c=Counter(hand)
        for x in sorted(c):
            need=c[x]
            if need:
                for y in range(x,x+groupSize):
                    if c[y]<need: return False
                    c[y]-=need
        return True