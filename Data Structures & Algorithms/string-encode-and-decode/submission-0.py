class Solution:

    def encode(self, strs: List[str]) -> str:
        curr = 0
        self.pos = []
        res = ""
        for s in strs:
            res += s
            self.pos.append((curr, curr + len(s) - 1))
            curr += len(s)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        for l, r in self.pos:
            res.append(s[l:r + 1])
        return res