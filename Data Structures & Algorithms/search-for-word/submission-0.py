class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        node = TrieNode()
        node.insert(word)
        visit = set()
        rows, cols = len(board), len(board[0])
        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children or (r, c) in visit):
                return False
            visit.add((r, c))
            node = node.children[board[r][c]]
            if node.isEnd:
                return True
            found = dfs(r - 1, c, node) or dfs(r + 1, c, node) or dfs(r, c - 1, node) or dfs(r, c + 1, node)
            visit.remove((r, c))

            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, node):
                    return True
        return False
