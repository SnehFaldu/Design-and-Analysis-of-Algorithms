from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]

        while len(result) < n:
            odd = []
            even = []

            for x in result:
                odd_value = 2 * x - 1
                even_value = 2 * x

                if odd_value <= n:
                    odd.append(odd_value)

                if even_value <= n:
                    even.append(even_value)

            result = odd + even

        return result
