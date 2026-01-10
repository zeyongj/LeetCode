class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2=len(s1), len(s2)
        if n1<n2:
            return self.minimumDeleteSum(s2, s1)
        dp = [[0]*(n2+1) for _ in range(2)]
        for x in range(n1-1, -1, -1):
            par=x&1
            prev=1-par
            for y in range(n2-1, -1, -1):
                if s1[x]==s2[y]:
                    dp[par][y]=ord(s1[x]) + dp[prev][y+1]
                else:
                    dp[par][y]=max(dp[prev][y], dp[par][y+1])
        AsciiSum = 0
        for c in s1: AsciiSum += ord(c)
        for c in s2: AsciiSum += ord(c)

        return AsciiSum - 2*dp[0][0]
        