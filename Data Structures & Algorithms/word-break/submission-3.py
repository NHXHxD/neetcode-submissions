class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordSet = set(wordDict)
        for i in range(n):
            if not dp[i]:
                continue
            
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet:
                    dp[j] = True
        return dp[n]