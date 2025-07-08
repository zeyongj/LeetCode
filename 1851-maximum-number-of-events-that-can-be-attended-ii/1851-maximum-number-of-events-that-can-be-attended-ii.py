import bisect

class Solution:

    def __init__(self):
        self.events = []

    # Cache decorator to memoize results of function calls
    @cache
    def solve(self, i, k):
        if i >= len(self.events): 
            return 0
        if k <= 0: 
            return 0
        
        # Retrieve start time, end time, and value of current event
        s, e, v = self.events[i]
        
        # Find the next event that starts after the current event ends
        j = bisect.bisect(self.events, [e+1])
        
        # We have two options: either take the current event or don't
        return max(v + self.solve(j, k - 1), self.solve(i + 1, k))

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()  # Sort events based on their start times
        self.events = events
        return self.solve(0, k)