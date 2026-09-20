class Solution:
    def strWithout3a3b(self, a, b):
        ans = []
        while a > 0 or b > 0:
            can_add_a = (
                a > 0 and
                not (len(ans) >= 2 and ans[-1] == 'a' and ans[-2] == 'a')
            )
            can_add_b = (
                b > 0 and
                not (len(ans) >= 2 and ans[-1] == 'b' and ans[-2] == 'b')
            )
            if can_add_a and (a >= b or not can_add_b):
                ans.append('a')
                a -= 1
            elif can_add_b:
                ans.append('b')
                b -= 1
            else:
                break
        return ''.join(ans)