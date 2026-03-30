class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for n in hand:
            if count[n]:
                for c in range(n, n + groupSize):
                    if not count[c]:
                        return False
                    count[c] -= 1
        return True