class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        res = 1
        wordList.append(beginWord)
        adj = defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                p = w[:j] + "*" + w[j + 1:]
                adj[p].append(w)

        visit = set([beginWord])
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if curr == endWord:
                    return res

                for j in range(len(curr)):
                    p = curr[:j] + "*" + curr[j + 1:]
                    for nei in adj[p]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)                    

            res += 1
        return 0