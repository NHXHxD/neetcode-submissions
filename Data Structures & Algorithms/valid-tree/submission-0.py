class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adjList = [[] for i in range(n)]
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
           
            for n in adjList[node]:
                if n == par:
                    continue
                if not dfs(n, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n