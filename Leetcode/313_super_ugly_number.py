class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1]
        indices = [0] * len(primes)
        values = primes[:]

        for _ in range(1, n):
            nxt = min(values)
            ugly.append(nxt)
            for i in range(len(primes)):
                if values[i] == nxt:
                    indices[i] += 1
                    values[i] = ugly[indices[i]] * primes[i]
        return ugly[-1]
