class Solution:
    def __init__(self):
        self.dp = [-1] * 366

    def solve(self, ind, days, costs):
        if ind >= len(days):
            return 0
        if self.dp[ind] != -1:
            return self.dp[ind]

        oneDay = costs[0] + self.solve(ind + 1, days, costs)

        sevenDayIndex = self.lower_bound(days, days[ind] + 7)
        sevenDays = costs[1] + self.solve(sevenDayIndex, days, costs)

        thirtyDayIndex = self.lower_bound(days, days[ind] + 30)
        thirtyDays = costs[2] + self.solve(thirtyDayIndex, days, costs)

        self.dp[ind] = min(oneDay, min(sevenDays, thirtyDays))
        return self.dp[ind]

    def lower_bound(self, arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low

    def mincostTickets(self, days, costs):
        self.dp = [-1] * 366
        return self.solve(0, days, costs)