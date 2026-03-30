class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        def check(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
 
        for l in range(n):
            r = l + 1
            a = check(l, l)
            b = check(l, r)
            if len(res) < len(a):
                res = a
            if len(res) < len(b):
                res = b
        return res              