public class Solution {
    public int UniquePaths(int m, int n)
        {
            // Matrix to store the value of possible ways to reach each cell
            int[][] dp = new int[m][];

            // C# thing, as we cannot define int[][] dp = new int[m][n]; 
            for (int i = 0; i < m; i++)
            {
                dp[i] = new int[n];
            }

            //Base Conditions 
            // all first column of every row as 1
            for(int i = 0; i < dp.Length; i++)
                dp[i][0] = 1;
            // all first row of every column as 1
            for(int i = 0; i< dp[0].Length; i++)
                  dp[0][i] = 1;

            for (int i = 1; i < m; i++)
            {
                for (int j = 1; j < n; j++)
                {
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];   
                }
            }

            return dp[m - 1][n - 1];

        }
}