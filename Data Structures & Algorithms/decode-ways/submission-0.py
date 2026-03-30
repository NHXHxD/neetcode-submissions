class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        # Empty suffix = one valid way
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            # A decoding cannot start with 0
            if s[i] == '0':
                dp[i] = 0
                continue

            # Take one digit
            dp[i] = dp[i + 1]

            # Take two digits if valid: 10..26
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                dp[i] += dp[i + 2]

        return dp[0]