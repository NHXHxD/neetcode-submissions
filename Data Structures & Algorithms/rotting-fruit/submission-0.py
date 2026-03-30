class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visit = set()
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while q and fresh > 0:
            res += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in directions:
                    nr, nc = x + r, y + c

                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        fresh -= 1
        
        return res if fresh == 0 else -1



            