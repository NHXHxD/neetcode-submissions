class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols =  len(heights), len(heights[0])
        atl_visit = set()
        pac_visit = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q_pac = deque()
        q_atl = deque()
        for r in range(rows):
            # pac left
            pac_visit.add((r, 0))
            q_pac.append((r, 0))
            
            # atl right
            atl_visit.add((r, cols - 1))
            q_atl.append((r, cols - 1))
            
        for c in range(cols):
            # pac top
            pac_visit.add((0, c))
            q_pac.append((0, c))
            
            # atl bottom
            atl_visit.add((rows - 1, c))
            q_atl.append((rows - 1, c))

        def bfs(q, visit):
            while q:
                cr, cc = q.popleft()
                
                for x, y in directions:
                    nr, nc = cr + x, cc + y
                    
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and heights[nr][nc] >= heights[cr][cc]:
                        visit.add((nr, nc))
                        q.append((nr, nc))

        bfs(q_pac, pac_visit)
        bfs(q_atl, atl_visit)

        return list(pac_visit & atl_visit)