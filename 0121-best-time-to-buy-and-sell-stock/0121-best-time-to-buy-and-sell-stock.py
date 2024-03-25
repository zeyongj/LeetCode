import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = math.inf
        
        size = len(prices)
        
        if size == 0:
            return 0
        
        for i in range(size):
            if prices[i] < min_price:
                min_price = prices[i]
            
            profit = prices[i] - min_price
            
            if profit > max_prof:
                max_prof = profit
        
        return max_prof
        
        