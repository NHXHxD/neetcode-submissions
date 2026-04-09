class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(ss):
            l, r = 0, len(ss) - 1
            while l < r:
                if ss[l] != ss[r]:
                    return False
                l += 1
                r -= 1
            return True
        curr = []
        res = []
        def dfs(start, path):
            if start == len(s):
                f = True
                for n in path:
                    if not check(n):
                        f = False
                if f:
                    res.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                path.append(s[start:end])
                dfs(end, path)
                path.pop()
        
        dfs(0, [])
        return res