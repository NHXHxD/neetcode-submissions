class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        i = 0
        res = []
        while i < len(s):
            start = i
            q = deque()
            c = Counter()
            seen = set()
            q.append(s[i])
            flag = False
            while q:
                curr = q.popleft()
                while c[curr] < count[curr]:
                    char = s[i]
                    c[char] += 1
                    if char not in seen:
                        seen.add(char)
                        q.append(char)
                        
                    i += 1
            res.append(i - start)
        return res
            