function minPathSum(G: number[][]): number {
    const M = G.length;
    const N = G[0].length;
    
    // Deep copy the G as the initial sum
    const dp = Array.from({length:M}, (_,m)=> Array.from({length:N}, (_,n) =>  G[m][n]));
    
    // Initial two border / boundary
    for(let i=M-2; i>=0; i--) {
        dp[i][N-1] = G[i][N-1] + dp[i+1][N-1];
    }
    for(let j = N-2; j>=0; j--) {
        dp[M-1][j] = G[M-1][j] + dp[M-1][j+1];
    }
    
    // DP
    for(let i=M-2; i>=0; i--) {
        for(let j = N-2; j>=0; j--) {
            dp[i][j] = G[i][j] + Math.min(dp[i+1][j], dp[i][j+1])
        }
    }
    return dp[0][0];
    
};