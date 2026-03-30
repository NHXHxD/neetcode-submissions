class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            r = 0
            while n > 0:
                if n & 1:
                    r += 1
                n >>= 1
            return r
        res = []
        for i in range(n + 1):
            res.append(count(i))
        return res