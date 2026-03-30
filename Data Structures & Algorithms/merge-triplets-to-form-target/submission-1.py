class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        while len(triplets) >= 2:
            one, two = triplets.pop(), triplets.pop()
            if one[0] > target[0] or one[1] > target[1] or one[2] > target[2]:
                triplets.append(two)
                continue

            if two[0] > target[0] or two[1] > target[1] or two[2] > target[2]:
                triplets.append(one)
                continue
            new = [max(one[0], two[0]), max(one[1], two[1]), max(one[2], two[2])]
            if new[0] == target[0] and new[1] == target[1] and new[2] == target[2]:
                return True
            triplets.append(new)
        if triplets:
            one, two, three = triplets.pop()
            if one == target[0] and two == target[1] and three == target[2]:
                return True
        return False