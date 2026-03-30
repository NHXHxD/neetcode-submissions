class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        res = 0
        r = len(heights) - 1
        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                l += 1
        return res