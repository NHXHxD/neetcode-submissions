import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        dist = [float('inf')] * (n + 1)
        for src, dst, w in times:
            adj[src].append((dst, w))
        q = [(0, k)]
        dist[k] = 0
        while q:
            w, u = heapq.heappop(q)
            if w > dist[u]:
                continue
            for v, weight in adj.get(u):
                if w + weight < dist[v]:
                    dist[v] = w + weight
                    heapq.heappush(q, (dist[v], v))
        res = max(dist[1:])
        return res if res != float('inf') else -1