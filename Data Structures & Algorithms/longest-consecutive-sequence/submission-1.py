import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        c = 1
        heapq.heapify(nums)
        prev = heapq.heappop(nums)
        while nums:
            curr = heapq.heappop(nums)
            if curr == prev:
                continue
            if curr != prev + 1:
                res = max(res, c)
                c = 1
            else:
                c += 1
            prev = curr
        return max(res, c)