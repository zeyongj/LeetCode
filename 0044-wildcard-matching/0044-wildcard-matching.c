#include <stdbool.h>
#include <string.h>

bool isMatch(char * s, char * p) {
    int m = strlen(s);
    int n = strlen(p);

    bool dp[m + 1][n + 1];
    memset(dp, false, sizeof(dp));

    // base cases
    dp[0][0] = true;
    for (int j = 1; j <= n; ++j) {
        if (p[j - 1] != '*') break;
        dp[0][j] = true;
    }

    // dynamic programming
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (p[j - 1] == '*') {
                dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
            } else if (p[j - 1] == '?' || s[i - 1] == p[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            }
        }
    }

    return dp[m][n];
}
