class Solution:
    def maxAmount(self, initialCurrency: str, 
            pairs1: List[List[str]], rates1: List[float],
            pairs2: List[List[str]], rates2: List[float]) -> float:
        
        m, n = len(pairs1), len(pairs2)
        dp = defaultdict(int)
        dp[initialCurrency] = 1.00
        
        for pair in product(range(m), range(m)):    # <-- Day 1
            (start, target), rate = pairs1[pair[1]], rates1[pair[1]]

            dp[target] = max(dp[target], dp[start ]*rate)
            dp[start ] = max(dp[start ], dp[target]/rate)

        for pair in product(range(n), range(n)):    # <-- Day 2
            (start, target), rate = pairs2[pair[1]], rates2[pair[1]]

            dp[target] = max(dp[target], dp[start ]*rate)
            dp[start ] = max(dp[start ], dp[target]/rate)

        return dp[initialCurrency]