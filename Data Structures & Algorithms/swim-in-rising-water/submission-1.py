class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        heap = []
        visit = set()
        visit.add((0, 0))
        rows = len(grid)
        heapq.heappush(heap, (grid[0][0], 0, 0))
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == rows -1: 
                return t
            for x, y in directions:
                nr, nc = r + x, c + y
                if nr not in range(rows) or nc not in range(rows) or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))

 