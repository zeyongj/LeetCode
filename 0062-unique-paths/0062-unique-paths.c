int uniquePaths(int m, int n){
    int dp[m+1][n+1];
    for(int i=0; i<m+1; i++)
        for(int j=0; j<n+1; j++)
        {
            if(i==1 || j==1)
                dp[i][j] = 1;
            else
                dp[i][j] = 0;
        }
    for(int i=2; i<=m; i++)
        for(int j=2; j<=n; j++)
        {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    return dp[m][n];
}
