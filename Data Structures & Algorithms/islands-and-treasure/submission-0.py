class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()

        inf = 2**31 - 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            cR, cC = q.popleft()

            for nr, nc in directions:
                newR, newC = cR + nr, cC + nc
                
                if newR in range(rows) and newC in range(cols) and grid[newR][newC] == inf:
                    q.append((newR, newC))
                    grid[newR][newC] = grid[cR][cC] + 1
                


                    
        
        