class PrefixTree:
    def __init__(self):
        self.isEnd = False
        self.children = {}

    def insert(self, word: str) -> None:
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTree()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        