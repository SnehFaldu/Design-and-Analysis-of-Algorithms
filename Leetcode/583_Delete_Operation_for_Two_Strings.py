class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Minimum deletions = len(word1) + len(word2) - 2 * LCS length.
        previous = [0] * (len(word2) + 1)
        for char1 in word1:
            current = [0] * (len(word2) + 1)
            for j, char2 in enumerate(word2, start=1):
                if char1 == char2:
                    current[j] = previous[j - 1] + 1
                else:
                    current[j] = max(previous[j], current[j - 1])
            previous = current
        return len(word1) + len(word2) - 2 * previous[-1]