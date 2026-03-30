import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        key = list(count.keys())
        key.sort(key=lambda x: count[x], reverse=True)
        return key[:k]