from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # after 1st buy, profit is negative cost of that buy
        first_buy = float('-inf')
        # after 1st sell, profit is best gain from one transaction
        first_sell = 0
        # after 2nd buy, profit is best leftover from first profit minus cost of second buy
        second_buy = float('-inf')
        # after 2nd sell, profit is best gain from two transactions
        second_sell = 0

        for p in prices:
            # maximize profit after first buy (i.e. buy at lowest price)
            first_buy = max(first_buy, -p)
            # maximize profit after first sell
            first_sell = max(first_sell, first_buy + p)
            # maximize profit after second buy (reinvest first_sell)
            second_buy = max(second_buy, first_sell - p)
            # maximize profit after second sell
            second_sell = max(second_sell, second_buy + p)

        return second_sell
