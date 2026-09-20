class Solution:
    def mctFromLeafValues(self, arr):
        stack = [float('inf')]
        cost = 0
        for x in arr:
            while stack[-1] <= x:
                mid = stack.pop()
                cost += mid * min(stack[-1], x)
            stack.append(x)
        while len(stack) > 2:
            cost += stack.pop() * stack[-1]
        return cost