class Twitter:

    def __init__(self):
        self.time = -1
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        users = set(self.follows[userId])
        users.add(userId)

        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (time, tweetId, uid, idx - 1))
        
        while heap and len(res) < 10:
            time, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)
            
            if idx >= 0:
                next_time, next_tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (next_time, next_tweetId, uid, idx - 1))
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
