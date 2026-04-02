class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        def dfs(i,  curr):
            if i >= len(nums):
                return 1 if curr == target else 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            
            return dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
        return dfs(0, 0)