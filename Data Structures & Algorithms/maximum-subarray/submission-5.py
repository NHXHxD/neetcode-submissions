class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        res = nums[0]
        for i in range(len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            res = max(res, curr)

        return res