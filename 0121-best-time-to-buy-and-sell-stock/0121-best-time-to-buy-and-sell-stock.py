import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic Programming:
        # For each day, you decide whether to sell the stock on this day or not. If you decide to sell, you need to have bought it at the minimum price seen so far.
        # dp[i] captures the maximum profit up to day i, ensuring that at each step, you're building upon the solutions to the subproblems (maximum profit up to the previous day and the minimum price seen so far).
        size = len(prices)
        
        if size == 0:
            return 0
        
        min_price = math.inf
        
        dp = [0]*size
        
        for i in range(size):
            if prices[i] < min_price:
                min_price = prices[i]
            
            profit = prices[i] - min_price
            
            dp[i] = max(profit, dp[i-1]) 
            
            # If we don't sell the stock on day i, the maximum profit is the same as the maximum profit up to day i-1, which is dp[i-1].
            # If we sell the stock on day i, we need to have bought it on a previous day at the minimum price seen so far. The profit from this transaction is prices[i] - min_price. The maximum profit up to day i would then be this profit.
        
        return dp[-1]
        
        
#         # Loop Method:
#         max_prof = 0
#         min_price = math.inf
        
#         size = len(prices)
        
#         if size == 0:
#             return 0
        
#         for i in range(size):
#             if prices[i] < min_price:
#                 min_price = prices[i]
            
#             profit = prices[i] - min_price
            
#             if profit > max_prof:
#                 max_prof = profit
        
#         return max_prof
        
        