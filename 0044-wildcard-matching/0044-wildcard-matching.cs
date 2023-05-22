public class Solution {
    public bool IsMatch(string s, string p) {
        int m = s.Length;
        int n = p.Length;
        bool[,] dp = new bool[m + 1, n + 1];

        // base cases
        dp[0, 0] = true;
        for (int j = 1; j <= n; ++j) {
            if (p[j - 1] != '*') break;
            dp[0, j] = true;
        }

        // dynamic programming
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (p[j - 1] == '*') {
                    dp[i, j] = dp[i - 1, j] || dp[i, j - 1];
                } else if (p[j - 1] == '?' || s[i - 1] == p[j - 1]) {
                    dp[i, j] = dp[i - 1, j - 1];
                }
            }
        }

        return dp[m, n];
    }
}