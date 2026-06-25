class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        f = 0
        for i in range(1, len(nums) + 1):
            f += i
        for n in nums:
            f -= n
        return f