from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for value, count in freq.items():
            buckets[count].append(value)

        answer = []

        for count in range(len(buckets) - 1, 0, -1):
            for value in buckets[count]:
                answer.append(value)
                if len(answer) == k:
                    return answer

        return answer
