class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = []

        def computePalindromes():
            for len in range(1, n+1):
                for i in range(n-len+1):
                    j = i + len - 1
                    condition = (s[i] == s[j]) and (len <= 2 or dp[i+1][j-1])
                    dp[i][j] = condition
        
        def backtrack(index, curr):
            if index >= n: 
                result.append(list(curr))
            for i in range(index, n):
                if dp[index][i]:
                    curr.append(s[index:i + 1])
                    backtrack(i + 1, curr)
                    curr.pop()

        computePalindromes()
        backtrack(0, [])
        return result