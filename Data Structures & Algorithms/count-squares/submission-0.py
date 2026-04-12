class CountSquares:

    def __init__(self):
        self.pts = []
        self.m = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.m[(point[0], point[1])] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for x1, y1 in self.pts:
            if abs(x1 - x) != abs(y1 - y):
                continue
            if x1 == x and y1 == y:
                continue
            res += self.m[(x1, y)] * self.m[(x, y1)]

        return res