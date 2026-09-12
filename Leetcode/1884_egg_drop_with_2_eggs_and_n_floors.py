class Solution:
    def twoEggDrop(self, n):
        moves = 0
        covered = 0
        while covered < n:
            moves += 1
            covered += moves
        return moves
