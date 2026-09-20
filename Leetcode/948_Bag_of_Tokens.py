class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort(); l,r=0,len(tokens)-1; score=best=0
        while l<=r:
            if power>=tokens[l]: power-=tokens[l]; l+=1; score+=1; best=max(best,score)
            elif score and l<r: power+=tokens[r]; r-=1; score-=1
            else: break
        return best