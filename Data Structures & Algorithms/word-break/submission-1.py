
class TrieNode:
    def __init__(self):
        self.children = {}   # maps char -> TrieNode
        self.is_end = False  # marks end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for k in wordDict:
            trie.insert(k)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            node = trie.root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]

                if node.is_end:
                    dp[j + 1] = True
        return dp[n]
