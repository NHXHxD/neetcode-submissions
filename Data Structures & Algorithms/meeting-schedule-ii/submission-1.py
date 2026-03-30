"""
Definition of Interval:
class Inter val(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        groups = []
        intervals.sort(key=lambda x:x.start)
        for i in intervals:
            f = False
            for g in groups:
                l = g[len(g) - 1]
                if i.start >= l.end:
                    f = True
                    g.append(i)
                    break
            if not f:
                g = []
                g.append(i)
                groups.append(g)
                
        return len(groups)

