class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph=defaultdict(list)
        for required,course in relations:
            graph[course].append(required)

        @cache
        def dp (i):
            if not graph.get(i,False):
                return time[i-1]
            ans=-1
            for j in graph[i]:
                ans=max(ans,dp(j))
            return ans+time[i-1]
        return max([dp(i+1) for i in range(n)])