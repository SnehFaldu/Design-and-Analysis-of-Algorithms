import heapq

class Solution:
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        INF = 10**30
        dist = [INF] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        heap = [(0, 0)]

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue

            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(heap, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[-1]
