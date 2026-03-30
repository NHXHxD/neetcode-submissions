class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [-1] * len(nums)
        dp2 = [-1] * len(nums)
        if len(nums) == 1:
            return nums[0]
        def dfs1(i):
            if i == len(nums) - 1:
                return 0
            elif i >= len(nums):
                return 0
            if dp1[i] != -1:
                return dp1[i]
            dp1[i] = max(nums[i] + dfs1(i + 2), dfs1(i + 1))
            return dp1[i]
        def dfs2(i):
            if i >= len(nums):
                return 0
            if dp2[i] != -1:
                return dp2[i]
            dp2[i] = max(nums[i] + dfs2(i + 2), dfs2(i + 1))
            return dp2[i]
        return max(dfs1(0), dfs2(1))