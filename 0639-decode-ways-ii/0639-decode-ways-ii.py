class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i] = number of ways to decode s[0:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has 1 way
        
        # Helper function to count single digit decodings
        def single_digit_ways(c):
            if c == '*':
                return 9  # Can be 1-9
            elif c == '0':
                return 0  # Invalid
            else:
                return 1  # Valid single digit
        
        # Helper function to count two digit decodings
        def two_digit_ways(c1, c2):
            if c1 == '*' and c2 == '*':
                # ** can be 11-19 (9 ways) and 21-26 (6 ways)
                return 15
            elif c1 == '*':
                # *X where X is a digit
                if c2 <= '6':
                    return 2  # Can be 1X or 2X
                else:
                    return 1  # Can only be 1X
            elif c2 == '*':
                # X* where X is a digit
                if c1 == '1':
                    return 9  # 11-19
                elif c1 == '2':
                    return 6  # 21-26
                else:
                    return 0  # 3*-9* are invalid
            else:
                # Both are digits
                num = int(c1 + c2)
                if 10 <= num <= 26:
                    return 1
                else:
                    return 0
        
        # Base case: first character
        dp[1] = single_digit_ways(s[0])
        
        for i in range(2, n + 1):
            # Single digit decoding
            dp[i] = (dp[i] + dp[i-1] * single_digit_ways(s[i-1])) % MOD
            
            # Two digit decoding
            dp[i] = (dp[i] + dp[i-2] * two_digit_ways(s[i-2], s[i-1])) % MOD
        
        return dp[n]