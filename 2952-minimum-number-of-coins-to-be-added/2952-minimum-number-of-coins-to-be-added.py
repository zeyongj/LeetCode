class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        
        extraCoins = reachable = 0
        for coin in coins:
            while reachable < (coin - 1):
                reachable = 2 * reachable + 1
                extraCoins += 1
            reachable += coin
        
        while reachable < target:
            reachable = 2 * reachable + 1
            extraCoins += 1 
        
        return extraCoins