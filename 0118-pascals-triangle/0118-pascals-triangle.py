class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        
        for i in range(1, numRows):
            temp = [1] * (i+1)
            dp.append(temp)
        
        for i in range(2, numRows):
            j = 1
            while (j < i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                j += 1
        
        return dp
        
        
        
        