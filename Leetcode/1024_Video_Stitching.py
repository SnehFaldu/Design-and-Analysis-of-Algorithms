class Solution:
    def videoStitching(self, clips, time):
        clips.sort(); i=end=farthest=ans=0
        while end<time:
            while i<len(clips) and clips[i][0]<=end:
                farthest=max(farthest,clips[i][1]); i+=1
            if farthest==end: return -1
            end=farthest; ans+=1
        return ans