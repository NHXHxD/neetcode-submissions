class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c = 0
        for n in range(len(nums) + 1):
            c ^= n
        for num in nums:
            c ^= num
        return c