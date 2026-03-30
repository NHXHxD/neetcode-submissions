class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        par = [i for i in range(n)]
        rank = [1] * n
        def find(p):
            p = par[p]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += p2
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                edges.append((abs(x1 - x2) + abs(y1 - y2),i, j))
        mst = set()
        edges.sort()
        res = 0
        i = 0
        while len(mst) < n - 1:
            w, u, v = edges[i]
            if union(u, v):
                mst.add((u, v))
                res += w
            i += 1
        return res