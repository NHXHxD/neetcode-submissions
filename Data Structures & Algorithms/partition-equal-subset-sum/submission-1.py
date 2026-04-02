class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        dp = {}
        def dfs(i, curr):
            if i >= len(nums) or curr > total // 2:
                return False
            if 2 * curr == total:
                return True
            if (i, curr) in dp:
                return dp[(i, curr)]
            dp[(i, curr)] = dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr)
            return dp[(i, curr)]

        return dfs(0, 0)