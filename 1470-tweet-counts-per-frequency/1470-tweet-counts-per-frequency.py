from sortedcontainers import SortedList


class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(lambda: SortedList())
        
    def recordTweet(self, tweet_name: str, time: int) -> None:
        self.tweets[tweet_name].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweet_name: str, start_time: int, end_time: int) -> List[int]:
        t = start_time
        dt = {"minute": 60, "hour": 3600, "day": 86400}[freq]
        counts = []
        while t <= end_time:
            t_end = min(end_time, t + dt - 1)
            s = self.tweets[tweet_name].bisect_left(t)
            e = self.tweets[tweet_name].bisect_right(t_end)
            counts.append(e - s)

            t += dt
        return counts



# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)