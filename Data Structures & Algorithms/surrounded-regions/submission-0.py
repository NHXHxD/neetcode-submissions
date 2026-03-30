class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        def dfs(r, c):
            if (r, c) in visit or r not in range(rows) or c not in range(cols) or board[r][c] == "x":
                return

            if (r, c) not in visit and r in range(rows) and c in range(cols) and board[r][c] == "O":
                board[r][c] = "#"
                visit.add((r, c))
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)
            
        rows = len(board)
        cols = len(board[0])
    
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
            
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"
