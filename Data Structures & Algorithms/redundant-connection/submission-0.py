class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = [[] for _ in range(n + 1)]
        def dfs(node, par):
            if visit[node]:
                return True
            
            visit[node] = True
            for n in adjList[node]:
                if n == par:
                    continue
                if dfs(n, node):
                    return True
            return False
        
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            visit = [False] * (n + 1)
            if dfs(u, -1):
                return [u, v]
        return []