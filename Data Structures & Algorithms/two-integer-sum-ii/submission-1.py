class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin(num):
            l = 0
            r = len(numbers) - 1
            while l <= r:
                m = (l + r) // 2
                if num > numbers[m]:
                    l = m + 1
                elif num < numbers[m]:
                    r = m - 1
                else:
                    return m
            return -1
        for i, num in enumerate(numbers):
            f = bin(target - num)
            if f != -1 and i != f:
                return [i + 1, f + 1]