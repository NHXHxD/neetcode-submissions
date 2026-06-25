class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)
        res = -1
        for c, chars in idx.items():
            if len(chars) >= 2:
                res = max(res, chars[-1] - chars[0] + 1 - 2)
        return res