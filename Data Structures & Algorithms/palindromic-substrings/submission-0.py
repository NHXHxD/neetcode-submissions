class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        seen = set()
        def check(l, r):
        
            curr = 0
            while l >= 0 and r < n and s[l] == s[r]:
                if (l, r) not in seen:
                    curr += 1
                seen.add((l, r))
                l -= 1
                r += 1

            return curr
 
        for l in range(n):
            r = l + 1
            res += check(l, l)
            res += check(l, r)
            
        return res              