class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        if neg:
            x = x * -1
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        if res not in range(-2**31, 2**31):
            return 0
        return res if not neg else res * -1