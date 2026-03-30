class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        adjList = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            if src not in adjList:
                adjList[src] = []
            adjList[src].append(dst)

        def dfs(node):
            if node in visit:
                return False
            if adjList[node] == []:
                return True
            visit.add(node)
            for n in adjList[node]:
                if not dfs(n):
                    return False
            visit.remove(node)
            adjList[node] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
