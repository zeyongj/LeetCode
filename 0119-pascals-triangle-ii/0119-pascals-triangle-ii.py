class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]]
        
        for i in range(1, rowIndex + 1):
            dp.append([1] * (i+1))
        
        for i in range(2, rowIndex + 1):
            j = 1
            while (j < i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                j += 1
        
        return dp[rowIndex]