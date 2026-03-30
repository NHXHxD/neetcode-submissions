class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != 0:
                return dp[i]
            dp[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            return nums[i] + max(dfs(i + 2), dfs(i + 3))
        return max(dfs(0),dfs(1))