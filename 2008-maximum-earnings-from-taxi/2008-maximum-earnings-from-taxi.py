from bisect import bisect_right
from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])  # Sort by end time
        dp = [(0, 0)]  # (position, max_profit_up_to_that_position)
        positions = [0]
        
        for starti, endi, tipi in rides:
            i = bisect_right(positions, starti)
            if i == 0:
                dp_i = 0
            else:
                dp_i = dp[i - 1][1]
            profit = dp_i + (endi - starti + tipi)
            if profit > dp[-1][1]:
                dp.append((endi, profit))
                positions.append(endi)
        return dp[-1][1]
