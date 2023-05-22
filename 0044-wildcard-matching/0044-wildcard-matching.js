/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let m = s.length, n = p.length;
    let dp = Array(m+1).fill().map(() => Array(n+1).fill(false));
    
    // base cases
    dp[0][0] = true;
    for (let j = 1; j <= n; j++) {
        if (p[j - 1] !== '*') break;
        dp[0][j] = true;
    }
    
    // dynamic programming
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (p[j - 1] === '*') {
                dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
            } else if (p[j - 1] === '?' || s[i - 1] === p[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            }
        }
    }
    
    return dp[m][n];
};
