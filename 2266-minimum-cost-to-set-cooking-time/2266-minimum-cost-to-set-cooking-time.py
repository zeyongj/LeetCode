class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(mins, secs):
            if mins > 99 or secs > 99 or mins < 0 or secs < 0: return float('inf')
            s, curr, res = str(mins * 100 + secs), str(startAt), 0
            for ch in s:
                if ch == curr: res += pushCost
                else:
                    res += (pushCost + moveCost)
                    curr = ch
            return res

        mins, secs = targetSeconds // 60, targetSeconds % 60
        return min(cost(mins, secs), cost(mins - 1, secs + 60))