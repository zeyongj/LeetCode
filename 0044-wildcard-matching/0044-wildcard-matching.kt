class Solution {
    fun isMatch(s: String, p: String): Boolean {
        val m = s.length
        val n = p.length
        val dp = Array(m + 1) { BooleanArray(n + 1) }

        // base cases
        dp[0][0] = true
        for (j in 1..n) {
            if (p[j - 1] != '*') break
            dp[0][j] = true
        }

        // dynamic programming
        for (i in 1..m) {
            for (j in 1..n) {
                if (p[j - 1] == '*') {
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1]
                } else if (p[j - 1] == '?' || s[i - 1] == p[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]
                }
            }
        }

        return dp[m][n]
    }
}
